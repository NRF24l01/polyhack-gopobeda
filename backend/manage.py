from flask import Flask
from config import *
from flask_migrate import Migrate
from models import db
from flask_jwt_extended import JWTManager, create_access_token
from flask_cors import CORS
from datetime import timedelta
from  methods import create_user_method

app = Flask(__name__)
CORS(app, supports_credentials=True)

# Configs
app.config["SECRET_KEY"] = RANDOM_SECRET
app.config['FLASK_PYDANTIC_VALIDATION_ERROR_RAISE'] = True
app.config['JWT_SECRET_KEY'] = 'very_secret_config'
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=30)

# DB init
app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRES_CONN
migrate = Migrate(app, db)
db.init_app(app)


jwt = JWTManager(app)

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


def create_admin_user():
    user_obj = User(USERNAME, PASSWORD, EMAIL)
    user = create_user_method(user_obj, True)

    access_token = create_access_token(identity=user.user_id,
                                       additional_claims={"user_id": user.user_id, "access": "admin"})
    print(access_token)

    return access_token
