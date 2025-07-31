#!/usr/bin/env python3
"""
Module for Auth class
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """
    Auth class to manage the API authentication
    """
    def __init__(self) -> None:
        """
        Initialize Auth
        """
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Require authentication for a given path
        """
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        if path in excluded_paths or path + "/" in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Authorization header
        """
        if request is None or not request.headers.get("Authorization"):
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Current user
        """
        return None
