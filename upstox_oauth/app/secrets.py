import json

import boto3

from app.config import AWS_SECRET_NAME


def get_upstox_credentials() -> dict:

    client = boto3.client(
        "secretsmanager",
        region_name="ap-south-1",
    )

    response = client.get_secret_value(
        SecretId=AWS_SECRET_NAME
    )

    secret = json.loads(response["SecretString"])

    return {
        "client_id": secret["client_id"],
        "client_secret": secret["client_secret"],
    }