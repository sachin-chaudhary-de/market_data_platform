import requests
from datetime import date, timedelta

HISTORICAL_URL = "https://api.upstox.com/v3/historical-candle"


def fetch_historical_data(instrument_key: str,
                           unit: str,
                            interval: str,
                             to_date: str,
                              from_date: str,
                               access_token: str,
                               ):

    url = (f"{HISTORICAL_URL}/"
            f"{instrument_key}/"
            f"{unit}/"
            f"{interval}/"
            f"{to_date}/"
            f"{from_date}"
            )

    headers = {"Accept": "application/json",
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

def extract_historical_data(
    instrument_keys: list[str],
    start_date: str,
    end_date: str,
    unit: str,
    interval: str,
    access_token: str,
    ):

    date_ranges = generate_month_ranges(
        start_date,
        end_date,
        )

    historical_data = {}

    for instrument_key in instrument_keys:

        historical_data[instrument_key] = []

        for from_date, to_date in date_ranges:

            response = fetch_historical_data(
                instrument_key=instrument_key,
                unit=unit,
                interval=interval,
                to_date=to_date,
                from_date=from_date,
                access_token=access_token,
                )

            candles = response["data"]["candles"]

            historical_data[instrument_key].extend(candles)

    return historical_data