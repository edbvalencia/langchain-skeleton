import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv(), override=True)

API_KEY_OPENAPI = os.environ.get("API_KEY_OPENAPI")
