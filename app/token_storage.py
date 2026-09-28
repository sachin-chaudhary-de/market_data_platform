import json

import boto3

from app.config import UPSTOX_TOKEN_SECRET_NAME


client = boto3.client(
    "secretsmanager",
    region_name="ap-south-1",
)


def save_token(token_response: dict) -> None:

    client.put_secret_value(
        SecretId=UPSTOX_TOKEN_SECRET_NAME,
        SecretString=json.dumps(token_response),
    )


def load_token() -> dict:

    response = client.get_secret_value(
        SecretId=UPSTOX_TOKEN_SECRET_NAME,
    )

    return json.loads(response["SecretString"])