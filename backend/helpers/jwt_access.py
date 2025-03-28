from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from werkzeug.exceptions import  Forbidden
from functools import wraps


def check_jwt_access(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        current_user = get_jwt()
        if current_user["access"] == "organizer":
            return func(*args, **kwargs)
        raise Forbidden("cannot access organizer")

    wrapper.__name__ = func.__name__
    return wrapper