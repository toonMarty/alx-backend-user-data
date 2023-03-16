#!/usr/bin/env python3
"""
Setting up a basic Flask app
"""
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth


AUTH = Auth()

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    Returns a JSON payload
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """
    This view function implements the POST /users route
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except Exception as exc:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def session_login() -> str:
    """
    A login function that responds to the
    POST /sessions route
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if AUTH.valid_login(email, password):
        new_session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie('session_id', new_session_id)
        return response
    abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def session_logout():
    """
    Logs out a user from  a session
    """
    req_session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(req_session_id)

    if not user:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect('/')


@app.route('/profile', methods=['GET'], strict_slashes=False)
def user_profile() -> str:
    """
    Get a user profile
    """
    session_id_cookie = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id_cookie)

    if user:
        return jsonify({"email": user.email}), 200
    else:
        abort(403)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
