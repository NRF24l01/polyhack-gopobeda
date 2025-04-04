from flask_pydantic import ValidationError
from werkzeug.exceptions import NotFound, BadRequest, Conflict, Forbidden
from flask import jsonify
from .exeptions import IncorrectData
from flask_jwt_extended.exceptions import JWTDecodeError
import jwt

def get_first_error(e):
    errors = []

    if e.form_params:
        errors += e.form_params

    if e.query_params:
        errors += e.query_params

    if e.body_params:
        errors += e.body_params

    if e.path_params:
        errors += e.path_params

    if errors:
        error = errors[0]
        return f"{error['msg']}: {'.'.join(map(str, error['loc']))}"  # loc - указывает на поле ошибки
    return "Unknown validation error"

def creates_response(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValidationError as e:
            error_msg = get_first_error(e)
            print(error_msg)
            return jsonify({"error": "Validation error", "details": error_msg}), 400
        except ValueError as e:
            return jsonify({"error": "Invalid input", "details": str(e)}), 400
        except BadRequest:
            return jsonify({"error": "Bad request", "reason": "cant parse request"}), 400
        except Forbidden:
            return jsonify({"error": "Forbidden", "reason": "not access"}), 403
        except NotFound:
            return jsonify({"error": "Not found", "reason": "object not found"}), 404
        except Conflict:
            return jsonify({"error": "Conflict", "reason": "conflict"}), 409
        except IncorrectData:
            return jsonify({"error": "Unauthorized", "reason": "We don't have such a record."}), 401
        except JWTDecodeError:
            return jsonify({"error": "Forbidden", "reason": "Incorrect token"}), 403
        except jwt.exceptions.InvalidSignatureError:
            return jsonify({"error": "Unauthorized", "reason": "Signature verification failed"}), 401
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Unauthorized", "reason": "Token expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Unprocessable entity", "reason": "Invalid token"}), 422
        except Exception as e:
            print(e)
            return jsonify({"error": "Internal server error", "reason": str(e)}), 500

    wrapper.__name__ = func.__name__
    return wrapper
