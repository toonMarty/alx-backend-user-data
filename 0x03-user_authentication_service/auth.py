#!/usr/bin/env python3
"""
This module contains a function _hash_password
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """A method that takes in a password
    string and returns bytes
    """
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed
