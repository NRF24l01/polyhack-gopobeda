from flask import Blueprint, request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required
from schemas import *
from flask import jsonify
from flask_pydantic import validate
from werkzeug.security import generate_password_hash, check_password_hash
from helpers import *
from werkzeug.exceptions import BadRequest
from methods import *

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
@creates_response
def login():
    login_field = request.json.get('email', None)
    password = request.json.get('password', None)

    if login_field is None or password is None:
        raise BadRequest('Missing email or password')

    user = get_user_by_email(login_field)

    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({'message': 'Неверный логин или пароль'}), 401

    access_token = create_access_token(identity=user.user_id,
                                       additional_claims={"user_id": user.user_id, "access": "user"})

    return jsonify({"jwt": access_token}), 200


@auth.route("/register/user", methods=['POST'])
@creates_response
@validate()
def create_user(body: CreateUserRequest):
    user = create_user_method(body, False)

    return jsonify(user.as_dict()), 201


@auth.route("/register/organizer", methods=['POST'])
@creates_response
@validate()
def create_organizer(body: CreateUserRequest):
    user = create_user_method(body, True)

    return jsonify(user.as_dict()), 201
