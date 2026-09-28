import json

from storage.s3 import upload_json
from app.config import S3_BUCKET, INSTRUMENTS_S3_KEY
from storage.s3 import object_exists, upload_json
from datetime import date, datetime, timezone

def load_instruments(instruments):

    ingestion_date = date.today().isoformat()
    ingestion_ts = datetime.now(timezone.utc).isoformat()

    s3_key = (
        f"master_data/instruments/"
        f"ingestion_date={ingestion_date}/"
        f"complete.json"
    )

    if object_exists(
        bucket=S3_BUCKET,
        key=s3_key,
    ):
        print("Instrument data already exists for today")
        return

    data = json.dumps({
                    "ingestion_ts": ingestion_ts,
                    "records": instruments,}
                    )

    upload_json(
        data=data,
        bucket=S3_BUCKET,
        key=s3_key,
    )
