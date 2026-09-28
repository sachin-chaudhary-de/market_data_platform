import boto3


s3 = boto3.client("s3")


def upload_json(
    data: str,
    bucket: str,
    key: str,
):
    s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=data,
        ContentType="application/json",
    )