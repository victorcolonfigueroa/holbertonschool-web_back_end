#!/usr/bin/env python3
"""
Module for BasicAuth class
"""
import base64
from typing import TypeVar
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """
    BasicAuth class
    """
    def __init__(self) -> None:
        """
        Initialize BasicAuth
        """
        super().__init__()

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extract the Base64 part of the Authorization header
        for Basic Authentication
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ")[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """
        Decode the Base64 part of the Authorization header
        for Basic Authentication
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_header = base64.b64decode(base64_authorization_header)
            return decoded_header.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> tuple[str, str]:
        """
        Extract the user credentials
        from the decoded Base64 authorization header
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        return tuple(decoded_base64_authorization_header.split(":", 1))

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str
                                     ) -> TypeVar('User'):
        """
        Return the User instance based on his email and password
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            # Search for user by email
            users = User.search({'email': user_email})
        except Exception:
            return None

        if not users:
            return None

        # Get the first (and should be only) user with this email
        user = users[0]

        # Validate password
        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieve the User instance for a request using Basic Authentication
        """
        # Get the authorization header from the request
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        # Extract the Base64 part of the authorization header
        base64_header = self.extract_base64_authorization_header(auth_header)
        if base64_header is None:
            return None

        # Decode the Base64 authorization header
        decoded_header = self.decode_base64_authorization_header(base64_header)
        if decoded_header is None:
            return decoded_header

        # Extract user credentials from the decoded header
        user_email, user_pwd = self.extract_user_credentials(decoded_header)
        if user_email is None or user_pwd is None:
            return None

        # Get the user object from credentials
        user = self.user_object_from_credentials(user_email, user_pwd)
        return user
