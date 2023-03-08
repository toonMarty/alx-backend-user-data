#!/usr/bin/env python3
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
        if excluded_paths is not None:
            for idx in range(len(excluded_paths)):
                excluded_paths[idx] = excluded_paths[idx].rstrip('/')

        if path is not None:
            # st_path: string.tolerant_path
            st_path = path.rstrip('/')
            if st_path is None and st_path not in excluded_paths:
                return True
            if st_path in excluded_paths:
                return False
            if st_path is None and excluded_paths == []:
                return True
        if excluded_paths is None and excluded_paths == '':
            return True
        return True

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
