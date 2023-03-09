#!/usr/bin/env python3
"""
This module contains an empty class
SessionAuth
"""
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """
    The class definition for SessionAuth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        This method creates a session ID for a user_id
        Args:
            user_id(str): the user id
        Return:
            session_id(str): session id for a user id

        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        This method returns the user ID based on a Session ID
        Args:
            session_id (str):  the session id
        Return:
            user_id(str): the user id
        """
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        This method returns a User instance based on a cookie value
        Args:
            request: the request
        Return:
            User instance
        """
        cookie_val = self.session_cookie(request)
        user_id = self.user_id_for_session_id(cookie_val)
        return User.get(user_id)
