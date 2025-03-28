from dotenv import load_dotenv
import os

load_dotenv(".env")

# Server configs
SERVER_HOST, SERVER_PORT  = os.getenv('SERVER_ADDRESS', "0.0.0.0:8080").split(":")[0], int(os.getenv('SERVER_ADDRESS', "0.0.0.0:8080").split(":")[1])
RANDOM_SECRET = os.getenv('RANDOM_SECRET', 'secret.tssss')

# Redis configs
REDIS_HOST = os.getenv('REDIS_HOST', '127.0.0.1')
REDIS_PORT = os.getenv('REDIS_PORT', 6379)

# Postgres config
POSTGRES_HOST = os.getenv('POSTGRES_HOST', '127.0.0.1')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', 5432)
POSTGRES_USERNAME = os.getenv('POSTGRES_USERNAME', 'postgres')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'postgres')
POSTGRES_DATABASE = os.getenv('POSTGRES_DATABASE')
POSTGRES_CONN = f"postgresql://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{str(POSTGRES_PORT)}/{POSTGRES_DATABASE}"

# Debug config
APP_DEBUG = bool(int(os.getenv('APP_DEBUG', 0)))

UPLOADFLOADER = "images"
