#!/usr/bin/env python3
"""
Auth module
"""
from db import DB
from user import User
from bcrypt import hashpw, gensalt, checkpw
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4
from typing import Optional


def _hash_password(password: str) -> bytes:
    """
    Hash a password
    """
    return hashpw(password.encode('utf-8'), gensalt())


def _generate_uuid() -> str:
    """
    Generate a UUID
    """
    return str(uuid4())


class Auth:
    """
    Auth class to interact with the authentication database.
    """
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user
        """
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate a user's login credentials
        """
        try:
            user = self._db.find_user_by(email=email)
            return checkpw(password.encode('utf-8'), user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> Optional[str]:
        """
        Create a session for a user
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(
            self, session_id: Optional[str]) -> Optional[User]:
        """
        Return the user corresponding to the given session_id or None.

        If session_id is None or no matching user is found, return None.
        """
        if session_id is None:
            return None
        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """
        Destroy a user's session by setting session_id to None.

        Always returns None. If the user does not exist, do nothing.
        """
        try:
            self._db.update_user(user_id, session_id=None)
        except NoResultFound:
            return None
        except ValueError:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """
        Generate and store a reset token for the user with the given email.

        Raises ValueError if the user does not exist.
        Returns the reset token as a string.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError

        token = _generate_uuid()
        self._db.update_user(user.id, reset_token=token)
        return token

    def update_password(self, reset_token: str, password: str) -> None:
        """
        Update a user's password using a valid reset token.

        Finds the user by reset_token. If not found, raises ValueError.
        Otherwise, hashes the new password and updates the user's
        hashed_password, and clears the reset_token.
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError

        new_hashed = _hash_password(password)
        self._db.update_user(user.id,
                             hashed_password=new_hashed,
                             reset_token=None)
        return None