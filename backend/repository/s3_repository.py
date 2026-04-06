import boto3

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
            for bucket in response['Buckets']:
                print(bucket['Name'])
                bucket_found = True
        if not bucket_found:
            print("No buckets found.")
