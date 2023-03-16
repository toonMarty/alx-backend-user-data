#!/usr/bin/env python3
"""
Setting up a basic Flask app
"""
from flask import Flask, jsonify, request, abort
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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
