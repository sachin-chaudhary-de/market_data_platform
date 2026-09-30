import os

import boto3
from dotenv import load_dotenv

from ingestion.extraction.historical_data import (
    extract_historical_data,
)
from ingestion.extraction.nifty50 import (
    get_nifty50_instrument_keys,
)


load_dotenv()


AWS_REGION = os.getenv(
    "AWS_REGION",
    "ap-south-1",
)

SECRET_NAME = os.getenv(
    "UPSTOX_TOKEN_SECRET_NAME"
)


def get_access_token():

    client = boto3.client(
        "secretsmanager",
        region_name=AWS_REGION,
    )

    response = client.get_secret_value(
        SecretId=SECRET_NAME,
    )

    return response["SecretString"]


instrument_keys = get_nifty50_instrument_keys()

print(
    "Matched instruments:",
    len(instrument_keys),
)


access_token = get_access_token()


historical_data = extract_historical_data(
    instrument_keys=instrument_keys,
    start_date="2025-01-01",
    end_date="2025-01-31",
    unit="minutes",
    interval="15",
    access_token=access_token,
)


print(
    "Extracted instruments:",
    len(historical_data),
)


for instrument_key, candles in historical_data.items():

    print(
        instrument_key,
        "→",
        len(candles),
        "candles",
    )