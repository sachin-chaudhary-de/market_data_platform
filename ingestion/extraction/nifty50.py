import json
import os

import boto3
from dotenv import load_dotenv

from ingestion.extraction.nifty50_symbols import NIFTY50_SYMBOLS

load_dotenv()


S3_BUCKET = os.getenv("S3_BUCKET")
AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")
INSTRUMENTS_PREFIX = "master_data/instruments/"


def get_latest_instrument_file():

    s3 = boto3.client(
        "s3",
        region_name=AWS_REGION,
    )

    response = s3.list_objects_v2(
        Bucket=S3_BUCKET,
        Prefix=INSTRUMENTS_PREFIX,
    )

    files = [
        obj
        for obj in response.get("Contents", [])
        if obj["Key"].endswith("/complete.json")
    ]

    if not files:
        raise FileNotFoundError(
            "No instrument file found in S3"
        )

    return max(
        files,
        key=lambda obj: obj["LastModified"],
    )["Key"]


def get_instruments():

    s3 = boto3.client(
        "s3",
        region_name=AWS_REGION,
    )

    key = get_latest_instrument_file()

    response = s3.get_object(
        Bucket=S3_BUCKET,
        Key=key,
    )

    data = json.loads(
        response["Body"].read()
    )

    return data["records"]


def get_nifty50_instrument_keys():

    instruments = get_instruments()

    return [
        instrument["instrument_key"]
        for instrument in instruments
        if (
            instrument.get("exchange") == "NSE"
            and instrument.get("segment") == "NSE_EQ"
            and instrument.get("instrument_type") == "EQ"
            and instrument.get("trading_symbol") in NIFTY50_SYMBOLS
        )
    ]