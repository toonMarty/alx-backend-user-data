#!/usr/bin/env python3
"""
This module contains an empty class BasicAuth
that inherits from Auth
"""
import base64
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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str)\
            -> str:
        """
        This method returns the decoded value of a Base64 string
        Args:
            base64_authorization_header(str): the authorization header
        Returns:
            decoded value as a UTF-8 string else None
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            encoded_string = base64_authorization_header.encode('utf-8')
            data = base64.b64decode(encoded_string)
            simple_string = data.decode('utf-8')
            return simple_string
        except Exception:
            return None
