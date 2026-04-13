import boto3
# What was done so far: Created private key and secret key for AWS S3, created a bucket as well. 
# Then we installed aws cli and configured it with the access key and secret key, enabling us to authenticate and interact with ease.
class s3Repository:
    def __init__(self):
        self.s3_client = boto3.client('s3', region_name='eu-north-1') # Create an S3 Client
    def list_buckets(self):
        self.paginator = self.s3_client.get_paginator("list_buckets") # Create a paginator for listing buckets
        self.response_iterator = self.paginator.paginate(PaginationConfig={"PageSize": 50, 
                                                                          "StartingToken": None})
        
        # Iterate through the responses
        bucket_found = False
        for response in self.response_iterator:
            for val,bucket in enumerate(response['Buckets']):
                print(f'Bucket: {bucket["Name"]}')
                print(f'Index: {val}')
                bucket_found = True
            return response['Buckets']
        if not bucket_found:
            print("No buckets found.")
            return None

    def upload_file(self, file, bucket_name):
        try:
            resource = boto3.resource('s3')
            bucket = resource.Bucket(bucket_name)
            bucket.upload_file(file,f'test\\{file}')
        except Exception as e:
            print(f"An error occurred: {e}")