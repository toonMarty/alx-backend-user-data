#!/usr/bin/env python3
"""
This module contains class UserSession
"""
from models.base import Base


class UserSession(Base):
    """The class definition for UserSession
    """
    def __init__(self, *args: list, **kwargs: dict):
        """The constructor method that initializes
        instances of UserSession
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
