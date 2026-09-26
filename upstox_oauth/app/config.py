import os

from dotenv import load_dotenv


load_dotenv()


UPSTOX_CLIENT_ID = os.getenv("UPSTOX_CLIENT_ID")
UPSTOX_CLIENT_SECRET = os.getenv("UPSTOX_CLIENT_SECRET")
UPSTOX_REDIRECT_URI = os.getenv("UPSTOX_REDIRECT_URI")

UPSTOX_AUTH_URL = (
    "https://api.upstox.com/v2/login/authorization/dialog"
)

UPSTOX_TOKEN_URL = (
    "https://api.upstox.com/v2/login/authorization/token"
)