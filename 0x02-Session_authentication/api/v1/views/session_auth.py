#!/usr/bin/env python3
"""
This module contains a function that handles
all routes for session authentication
"""
import os

from flask import jsonify, request, abort

from api.v1.views import app_views
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'],
                 strict_slashes=False)
def route_login_handler() -> str:
    """
    This view function handles all routes for
    session authentication
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({'error': 'email missing'}), 400
    if not password:
        return jsonify({'error': 'password missing'}), 400

    try:
        user = User.search({'email': email})
    except Exception:
        user = []

    if len(user) > 0:
        pswd = user[0].is_valid_password(password)
        if not pswd:
            return jsonify({"error": "wrong password"}), 401
        from api.v1.app import auth
        session_id = auth.create_session(user[0].id)
        user_to_json = jsonify(user[0].to_json())
        cookie_key = os.getenv('SESSION_NAME')
        user_to_json.set_cookie(cookie_key, session_id)
        return user_to_json
    else:
        return jsonify({"error": "no user found for this email"}), 404


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout() -> str:
    """
    destroy session
    """
    from api.v1.app import auth
    if not auth.destroy_session(request):
        abort(404)
    return jsonify({}), 200
