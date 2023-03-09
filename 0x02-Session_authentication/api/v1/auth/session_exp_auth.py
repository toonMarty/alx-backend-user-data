#!/usr/bin/env python3
"""
This module contains a class SessionExpAuth that inherits
from SessionAuth
"""
from datetime import datetime, timedelta
import os

from api.v1.auth.session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """
    The Class definition for SessionExpAuth
    """

    def __init__(self):
        """
        This is the constructor that initializes instances
        of this class
        """
        try:
            self.session_duration = int(os.getenv("SESSION_DURATION"))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id: str = None) -> str:
        """
        This method creates a session id
        Args:
            user_id(str): the user id
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        value = {'user_id': user_id, 'created_at': datetime.now()}
        self.user_id_by_session_id[session_id] = value
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        This method returns a user id in a given session id
        Args:
            session_id(str): the session_id
        Return:
            user_id(str): the user_id
        """
        if session_id is None:
            return None
        if session_id not in self.user_id_by_session_id:
            return None
        session_dict = self.user_id_by_session_id[session_id]
        user_id = session_dict.get('user_id')
        if self.session_duration <= 0:
            return user_id
        if 'created_at' not in session_dict:
            return None
        create_at = session_dict.get('created_at')
        create_at += timedelta(0, self.session_duration)
        if create_at < datetime.now():
            return None
        return user_id
