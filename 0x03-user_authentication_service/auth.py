#!/usr/bin/env python3
"""
This module contains a function _hash_password
"""
import bcrypt
from sqlalchemy.exc import NoResultFound
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """A method that takes in a password
    string and returns bytes
    """
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Initializing an Auth instance"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        This method registers a user and returns a User
        object
        """
        try:
            exists = self._db.find_user_by(email=email)
            if exists:
                raise ValueError(f'User {email} already exists')
        except NoResultFound:
            pass

        hashed_pswd = _hash_password(password)
        saved_user = self._db.add_user(email=email,
                                       hashed_password=hashed_pswd)
        return saved_user
