"""
This module contains a class Auth that will
be the template for all authentication systems
implemented
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """
    The class definition for Auth
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        This method checks for authentication as a
        requirement
        Args:
            path(str): the path
            excluded_paths(List[str]): excluded paths
        Return:
            False(bool)
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        This method is the authorization header
        Args:
            request: a Flask request object
        Return:
            None

        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        This method implements the current user
        Args:
            request: a Flask request object
        Return:
            None
        """
        return None
