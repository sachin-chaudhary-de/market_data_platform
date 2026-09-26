import requests

from app.config import (
    UPSTOX_CLIENT_ID,
    UPSTOX_CLIENT_SECRET,
    UPSTOX_REDIRECT_URI,
    UPSTOX_TOKEN_URL,
)


def exchange_code_for_token(code: str) -> dict:

    payload = {
        "code": code,
        "client_id": UPSTOX_CLIENT_ID,
        "client_secret": UPSTOX_CLIENT_SECRET,
        "redirect_uri": UPSTOX_REDIRECT_URI,
        "grant_type": "authorization_code",
    }

    response = requests.post(
        UPSTOX_TOKEN_URL,
        data=payload,
    )

    response.raise_for_status()

    return response.json()