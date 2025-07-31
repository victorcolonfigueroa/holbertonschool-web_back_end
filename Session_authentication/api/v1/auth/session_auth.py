#!/usr/bin/env python3
"""
Module for SessionAuth class
"""
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """
    SessionAuth class that inherits from Auth
    """
    def __init__(self) -> None:
        """
        Initialize SessionAuth
        """
        super().__init__()
