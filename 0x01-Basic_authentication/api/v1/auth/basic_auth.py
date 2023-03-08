#!/usr/bin/env python3
"""
This module contains an empty class BasicAuth
that inherits from Auth
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    Class definition for BasicAuth
    """
    def extract_base64_authorization_header(self, authorization_header: str) \
            -> str:
        """
        This method returns the Base64 part of the Authorization header for a
        basic authentication
        Args:
            authorization_header(str): the authorization header
        Returns:
            None if authorization_header is None
            None if authorization_header is not a string
            None if authorization_header does not start by Basic
            else
                str: the value after Basic
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        else:
            return authorization_header[6:]
