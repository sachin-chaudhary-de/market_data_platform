import gzip
import json

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


INSTRUMENT_URL = (
    "https://assets.upstox.com/market-quote/instruments/exchange/complete.json.gz"
)

def create_session():

    retry = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[500, 502, 503, 504],
        allowed_methods=["GET"],
    )

    session = requests.Session()

    session.mount(
        "https://",
        HTTPAdapter(max_retries=retry),
    )

    return session

def download_instruments():

    session = create_session()

    response = session.get(
        INSTRUMENT_URL,
        timeout=30,
    )

    response.raise_for_status()

    return response.content



def parse_instruments(data: bytes):

    decompressed_data = gzip.decompress(data)

    return json.loads(decompressed_data)

def extract_instruments():

    raw_data = download_instruments()

    instruments = parse_instruments(raw_data)

    return instruments

