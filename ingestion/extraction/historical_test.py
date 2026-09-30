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


batches = extract_historical_data(
    instrument_keys=instrument_keys,
    start_date="2026-04-01",
    end_date="2026-04-30",
    unit="minutes",
    interval="15",
    access_token=access_token,
)

batch_count = 0

for batch in batches:

    batch_count += 1

    print(
        batch["instrument_key"],
        batch["from_date"],
        "→",
        batch["to_date"],
        "candles:",
        len(batch["candles"]),
    )

print("Total batches:", batch_count)