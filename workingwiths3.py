import boto3

s3=boto3.client('s3', region_name='eu-north-1')

response = s3.list_buckets()

print(response)
