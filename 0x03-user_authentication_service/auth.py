#!/usr/bin/env python3
"""
This module contains a function _hash_password
"""
import bcrypt
import uuid
from sqlalchemy.orm.exc import NoResultFound
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """A method that takes in a password
    string and returns bytes
    """
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed


def _generate_uuid() -> str:
    """
    Generates a UUID and returns its string representation
    """
    return str(uuid.uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """
        This method checks if a login is valid
        Args:
            email(str): the user's email
            password(str): the user's password
        Return:
                True(bool): if match is found
            else
                False(bool): no match found
        """
        try:
            exists = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'),
                                  exists.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """
        Returns the session ID of a user as a UUID
        string
        """
        try:
            find_user = self._db.find_user_by(email=email)
            find_user.session_id = _generate_uuid()
            return find_user.session_id
        except NoResultFound:
            pass

    def get_user_from_session_id(self, session_id: str) -> str:
        """
        Get a user based on the user's session_id
        """
        if session_id:
            try:
                user = self._db.find_user_by(session_id=session_id)
                return user
            except NoResultFound:
                pass
        return None

    def destroy_session(self, user_id: int) -> None:
        """
        Updates the corresponding user's session ID to None
        destroying a user's session
        """
        if user_id:
            self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """
        Generates a reset password token
        """
        user = self._db.find_user_by(email=email)

        if user:
            user_uuid = _generate_uuid()
            self._db.update_user(user.id, reset_token=user_uuid)
            return user_uuid
        else:
            raise ValueError
