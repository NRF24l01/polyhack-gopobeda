from models import Users, db
from helpers import IncorrectData
from werkzeug.exceptions import Conflict
from werkzeug.security import generate_password_hash


def get_user_by_email(email):
    user = Users.query.filter_by(email=email).first()
    if user is None:
        raise IncorrectData
    return user


def create_user_method(body, is_organizer):
    if Users.query.filter_by(email=body.email).first():
        raise Conflict('Email already registered')

    password_hash = generate_password_hash(body.password)
    user = Users(username=body.username, email=body.email, password_hash=password_hash,
                 is_organizer=is_organizer)

    db.session.add(user)
    db.session.commit()

    return user
