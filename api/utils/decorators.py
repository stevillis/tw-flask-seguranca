"""Decorators module."""
from functools import wraps

from flask import jsonify, make_response
from flask_jwt_extended import get_jwt, verify_jwt_in_request


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
