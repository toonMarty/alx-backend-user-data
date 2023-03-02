#!/usr/bin/env python3
"""
This module contains a function
hash_password that returns a salted,
hashed password
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    This function returns a salted hashed password
    given a string as input
    Args:
        password(str): a string representing a password
    """
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    This function checks whether a password is valid given
    a hashed_password and a password as inputs
    Args:
        hashed_password(bytes): a hashed password
        password(str): a string representing a password
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
