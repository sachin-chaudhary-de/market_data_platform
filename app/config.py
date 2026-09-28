import os

from dotenv import load_dotenv


load_dotenv()

UPSTOX_REDIRECT_URI = os.getenv("UPSTOX_REDIRECT_URI")
AWS_SECRET_NAME = os.getenv("AWS_SECRET_NAME")
UPSTOX_TOKEN_SECRET_NAME = os.getenv("UPSTOX_TOKEN_SECRET_NAME")


UPSTOX_AUTH_URL = (
    "https://api.upstox.com/v2/login/authorization/dialog"
)

UPSTOX_TOKEN_URL = (
    "https://api.upstox.com/v2/login/authorization/token"
)