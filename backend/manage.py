from flask import Flask
from config import *
from flask_migrate import Migrate
from models import db
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

# Configs
app.config["SECRET_KEY"] = RANDOM_SECRET
app.config['FLASK_PYDANTIC_VALIDATION_ERROR_RAISE'] = True
app.config['JWT_SECRET_KEY'] = 'very_secret_config'

# DB init
app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRES_CONN
migrate = Migrate(app, db)
db.init_app(app)

# redis_client = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)

jwt = JWTManager(app)
