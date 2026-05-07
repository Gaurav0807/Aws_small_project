import boto3

def list_bucket():
    s3 = boto3.client("s3")

    response = s3.list_buckets()

    return response["Buckets"]