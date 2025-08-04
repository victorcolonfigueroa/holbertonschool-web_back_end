#!/usr/bin/env python3
""" Module of Session authentication views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request, make_response
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login() -> str:
    """ POST /api/v1/auth_session/login
    Return:
      - User object JSON represented
      - 400 if email or password is missing
      - 404 if no user found for this email
      - 401 if wrong password
    """
    # Get email and password from form data
    email = request.form.get('email')
    password = request.form.get('password')
    
    # Check if email is missing or empty
    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400
    
    # Check if password is missing or empty
    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400
    
    # Retrieve the User instance based on the email
    try:
        users = User.search({'email': email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404
    
    # Check if no user found
    if not users:
        return jsonify({"error": "no user found for this email"}), 404
    
    # Get the first (and should be only) user with this email
    user = users[0]
    
    # Check if the password is valid
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    
    # Import auth only when needed to avoid circular import
    from api.v1.app import auth
    
    # Create a Session ID for the User ID
    session_id = auth.create_session(user.id)
    if session_id is None:
        abort(500)  # Internal server error if session creation fails
    
    # Create response with user data
    response = make_response(jsonify(user.to_json()))
    
    # Set the cookie to the response using SESSION_NAME environment variable
    session_name = getenv('SESSION_NAME')
    if session_name:
        response.set_cookie(session_name, session_id)
    
    return response
