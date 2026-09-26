import json
from pathlib import Path


TOKEN_FILE = Path("storage/token.json")


def save_token(token_response: dict) -> None:
    TOKEN_FILE.write_text(
        json.dumps(token_response, indent=2)
    )


def load_token() -> dict:
    return json.loads(
        TOKEN_FILE.read_text()
    )