#!/usr/bin/env python3
"""
Module for SessionAuth class
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
    SessionAuth class that inherits from Auth
    """
    user_id_by_session_id = {}

    def __init__(self) -> None:
        """
        Initialize SessionAuth
        """
        super().__init__()

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a Session ID for a user_id
        
        Args:
            user_id (str): The user ID for which to create a session
            
        Returns:
            str: The Session ID, or None if user_id is invalid
        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        
        # Generate a Session ID using uuid4()
        session_id = str(uuid.uuid4())
        
        # Store the user_id with session_id as key
        self.user_id_by_session_id[session_id] = user_id
        
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns a User ID based on a Session ID
        
        Args:
            session_id (str): The session ID to look up
            
        Returns:
            str: The User ID associated with the session ID, or None if invalid
        """
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        
        # Use .get() to access the dictionary value based on key
        return self.user_id_by_session_id.get(session_id)
