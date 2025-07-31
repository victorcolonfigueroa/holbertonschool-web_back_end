#!/usr/bin/env python3
"""
Module that encrypts passwords
"""


import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt

    Args:
        password: The password to hash

    Returns:
        A salted, hashed password, which is a byte string
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Check if the provided password matches the hashed password
    """
    return bcrypt.checkpw(password.encode(), hashed_password)