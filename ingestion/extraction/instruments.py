import gzip
import json

import requests


INSTRUMENT_URL = (
    "https://assets.upstox.com/market-quote/instruments/exchange/complete.json.gz"
)


def download_instruments():

    response = requests.get(INSTRUMENT_URL)

    response.raise_for_status()

    return response.content


def parse_instruments(data: bytes):

    decompressed_data = gzip.decompress(data)

    return json.loads(decompressed_data)

def extract_instruments():

    raw_data = download_instruments()

    instruments = parse_instruments(raw_data)

    return instruments
