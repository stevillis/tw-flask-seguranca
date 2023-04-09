"""Decorators module."""
from functools import wraps

from flask import jsonify, make_response, request
from flask_jwt_extended import get_jwt, verify_jwt_in_request

from api.services.user_service import get_user_by_api_key


def admin_required(fn):
    """Admin required decorator."""

    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims["roles"] != "admin":
            return make_response(
                jsonify("User without authorization to access the resource."), 403
            )

        return fn(*args, **kwargs)

    return wrapper


def api_key_required(fn):
    """API Key required decorator."""

    @wraps(fn)
    def wrapper(*args, **kwargs):
        api_key = request.args.get("api_key")
        if api_key and get_user_by_api_key(api_key):
            return fn(*args, **kwargs)

        return make_response(jsonify("Invalid API Key."), 401)

    return wrapper
