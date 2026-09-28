import json

from storage.s3 import upload_json


BUCKET = "upstox-raw-master-data"
S3_KEY = "master_data/instruments/complete.json"


def load_instruments(instruments):

    data = json.dumps(instruments)

    upload_json(
        data=data,
        bucket=BUCKET,
        key=S3_KEY,
    )