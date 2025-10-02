import os
import boto3
from botocore.exceptions import ClientError
import uuid

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
AWS_ENDPOINT = os.getenv("AWS_ENDPOINT_URL")
S3_BUCKET = os.getenv("k8s-elias1")

s3 = boto3.client("s3", region_name=AWS_REGION, endpoint_url=AWS_ENDPOINT)

def upload_avatar(upload_file):
    # generate unique filename
    ext = upload_file.filename.split(".")[-1]
    key = f"avatars/{uuid.uuid4().hex}.{ext}"
    try:
        s3.upload_fileobj(upload_file.file, S3_BUCKET, key, ExtraArgs={"ACL": "private", "ContentType": upload_file.content_type})
    except ClientError as e:
        raise RuntimeError("S3 upload failed") from e
    
    if AWS_ENDPOINT:
        # Localstack: construct url differently
        return f"{AWS_ENDPOINT}/{S3_BUCKET}/{key}"
    return f"https://{S3_BUCKET}.s3.{AWS_REGION}.amazonaws.com/{key}"

