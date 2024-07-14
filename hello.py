import uuid
import boto3
import os


s3 = boto3.resource('s3')
s3 = boto3.client('s3')
bucket_name = "python-sdk-sample-%s" % uuid.uuid4()
#print("Creating new bucket with name:", bucket_name)
#s3.create_bucket(Bucket=bucket_name)
print(s3.list_buckets())
s3.list_buckets().to_json()

# snippet-end:[python.example_code.s3.Hello]