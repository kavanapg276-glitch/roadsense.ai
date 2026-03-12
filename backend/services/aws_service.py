import boto3
import uuid
from botocore.exceptions import NoCredentialsError

S3_BUCKET = "roadsense-road-images"
S3_REGION = "ap-south-1"

s3 = boto3.client("s3")

def upload_file(file):

    try:
        filename = str(uuid.uuid4()) + ".jpg"

        s3.upload_fileobj(
            file,
            S3_BUCKET,
            filename,
            ExtraArgs={"ContentType": "image/jpeg"}
        )

        url = f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com/{filename}"

        return {
            "status": "success",
            "url": url
        }

    except NoCredentialsError:
        return {
            "status": "error",
            "message": "AWS credentials not configured"
        }
