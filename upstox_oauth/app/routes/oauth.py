from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse

from app.config import (
    UPSTOX_AUTH_URL,
    UPSTOX_CLIENT_ID,
    UPSTOX_REDIRECT_URI,
)
from app.services import exchange_code_for_token
from app.token_storage import save_token

router = APIRouter()


@router.get("/login")
def login():

    authorization_url = (
        f"{UPSTOX_AUTH_URL}"
        f"?response_type=code"
        f"&client_id={UPSTOX_CLIENT_ID}"
        f"&redirect_uri={UPSTOX_REDIRECT_URI}"
    )

    return RedirectResponse(url=authorization_url)


@router.get("/oauth/callback")
def oauth_callback(
    request: Request,
    code: str,
):

    token_response = exchange_code_for_token(code)

    save_token(token_response)

    return token_response