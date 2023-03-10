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
        if excluded_paths is None or excluded_paths == '':
            return True
        if path is not None:
            if path[len(path) - 1] is not '/':
                path += '/'
        if path is None:
            return True
        for item in excluded_paths:
            a_val = item.find('*')
            if a_val != -1 and len(path) >= len(item):
                p_cpy = path[: a_val]
                if p_cpy == item[: a_val]:
                    return False
            elif path == item:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        This method is the authorization header
        Args:
            request: a Flask request object
        Return:
            None

        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        else:
            return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """
        This method implements the current user
        Args:
            request: a Flask request object
        Return:
            None
        """
        return None
