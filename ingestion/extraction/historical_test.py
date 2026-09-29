import os
import boto3
import requests
from datetime import date, timedelta
from dotenv import load_dotenv

from ingestion.extraction.historical_data import extract_historical_data


load_dotenv()


HISTORICAL_URL = "https://api.upstox.com/v3/historical-candle"

SECRET_NAME = os.getenv("UPSTOX_TOKEN_SECRET_NAME")
AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")


def get_access_token():

    client = boto3.client(
        "secretsmanager",
        region_name=AWS_REGION,
    )

    response = client.get_secret_value(
        SecretId=SECRET_NAME,
    )

    return response["SecretString"]


def fetch_historical_data(
    instrument_key: str,
    unit: str,
    interval: str,
    to_date: str,
    from_date: str,
    access_token: str,
):

    url = (
        f"{HISTORICAL_URL}/"
        f"{instrument_key}/"
        f"{unit}/"
        f"{interval}/"
        f"{to_date}/"
        f"{from_date}"
    )

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=30,
    )

    response.raise_for_status()

    return response.json()


def generate_month_ranges(
    start_date: str,
    end_date: str,
):

    start = date.fromisoformat(start_date)
    end = date.fromisoformat(end_date)

    ranges = []

    current = start

    while current <= end:

        next_month = (
            current.replace(day=28) + timedelta(days=4)
        ).replace(day=1)

        month_end = min(
            next_month - timedelta(days=1),
            end,
        )

        ranges.append(
            (
                current.isoformat(),
                month_end.isoformat(),
            )
        )

        current = month_end + timedelta(days=1)

    return ranges



# INSTRUMENT_KEY = "NSE_EQ|INE848E01016"
INSTRUMENT_KEYS = [
    "NSE_EQ|INE848E01016",
    "NSE_EQ|INE585B01010",
]

UNIT = "minutes"
INTERVAL = "15"

START_DATE = "2025-01-01"
END_DATE = "2025-03-31"


access_token = get_access_token()

historical_data = extract_historical_data(
    instrument_keys=INSTRUMENT_KEYS,
    start_date=START_DATE,
    end_date=END_DATE,
    unit=UNIT,
    interval=INTERVAL,
    access_token=access_token,
)


for instrument_key, candles in historical_data.items():

    print(instrument_key)
    print("Candles:", len(candles))
    print("First:", candles[0])
    print("Last:", candles[-1])