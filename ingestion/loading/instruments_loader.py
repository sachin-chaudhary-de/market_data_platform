import json

from storage.s3 import upload_json
from app.config import S3_BUCKET, INSTRUMENTS_S3_KEY



def load_instruments(instruments):

    data = json.dumps(instruments)

    upload_json(
    data=data,
    bucket=S3_BUCKET,
    key=INSTRUMENTS_S3_KEY,
)