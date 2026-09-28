import boto3
from botocore.exceptions import ClientError


s3 = boto3.client("s3")


def upload_json(
    data: str,
    bucket: str,
    key: str,
):
    response = s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=data,
        ContentType="application/json",
    )

    return response


def object_exists(
    bucket: str,
    key: str,
) -> bool:

    try:
        s3.head_object(
            Bucket=bucket,
            Key=key,
        )

        return True

    except ClientError as e:

        if e.response["Error"]["Code"] == "404":
            return False

        raise