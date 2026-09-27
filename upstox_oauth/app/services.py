import requests

from app.config import (UPSTOX_REDIRECT_URI, UPSTOX_TOKEN_URL,)
from app.secrets import get_upstox_credentials

def exchange_code_for_token(code: str) -> dict:

    credentials = get_upstox_credentials()

    payload = {
        "code": code,
        "client_id": credentials["client_id"],
        "client_secret": credentials["client_secret"],
        "redirect_uri": UPSTOX_REDIRECT_URI,
        "grant_type": "authorization_code",
    }

    response = requests.post(
        UPSTOX_TOKEN_URL,
        data=payload,
    )

    response.raise_for_status()

    return response.json()