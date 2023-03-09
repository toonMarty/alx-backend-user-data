#!/usr/bin/env python3
"""
This module contains an empty class BasicAuth
that inherits from Auth
"""
import base64
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User


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
            to_string = data.decode('utf-8')
            return to_string
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """
        This method returns the user email and password from the Base64
        decoded value
        Args:
            decoded_base64_authorization_header (str): the decoded
            authorization header
        Returns:
            user email and password
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if not decoded_base64_authorization_header.__contains__(':'):
            return None, None

        # Improving method to allow password with :
        sep = decoded_base64_authorization_header.find(":")
        user = decoded_base64_authorization_header[:sep]
        pswd = decoded_base64_authorization_header[sep + 1:]
        return user, pswd

        # credentials_list = decoded_base64_authorization_header.split(':')
        # return credentials_list[0], credentials_list[1]

    def user_object_from_credentials(self, user_email: str, user_pwd: str) \
            -> TypeVar('User'):
        """
        This method returns the user instance based on his
        email and password
        Args:
            user_email (str): the user email
            user_pwd (str): the user password
        Return:
            The user instance
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            user = User.search({'email': user_email})
        except Exception:
            return None
        if len(user) == 0:
            return None
        pswd = user[0].is_valid_password(user_pwd)

        if not pswd:
            return None
        return user[0]

    def current_user(self, request=None) -> TypeVar('User'):
        """
        This method overloads Auth and retrieves the User instance
        for a request
        Args:
            request: the request
        Return:
            User instance for a request
        """
        header = self.authorization_header(request)
        auth = self.extract_base64_authorization_header(header)
        decoded_val = self.decode_base64_authorization_header(auth)
        credentials = self.extract_user_credentials(decoded_val)
        return self.user_object_from_credentials(credentials[0],
                                                 credentials[1])
