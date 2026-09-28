import json

from storage.s3 import upload_json
from app.config import S3_BUCKET, INSTRUMENTS_S3_KEY
from storage.s3 import object_exists, upload_json

def load_instruments(instruments):

    data = json.dumps(instruments)

    upload_json(
    data=data,
    bucket=S3_BUCKET,
    key=INSTRUMENTS_S3_KEY,
)

def load_instruments(instruments):

    if object_exists(bucket=S3_BUCKET,
                    key=INSTRUMENTS_S3_KEY,):
        print("Instrument data already exists in S3")
        return

    data = json.dumps(instruments)

    upload_json(
        data=data,
        bucket=S3_BUCKET,
        key=INSTRUMENTS_S3_KEY,
    )