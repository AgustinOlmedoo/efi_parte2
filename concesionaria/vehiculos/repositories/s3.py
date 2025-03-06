import os
import boto3
import logging
from botocore.exceptions import ClientError

class S3Repository:
    s3_client = boto3.client(
        's3',
        #aws_access_key_id=os.getenv('#tu propia info'),
        #aws_secret_access_key=os.getenv('#tu propia info')
    )
    
    def upload_file(self, file_name, bucket, object_name=None):
        if object_name is None:
            object_name = os.path.basename(file_name)
        
        try:
            self.s3_client.upload_file(file_name, bucket, object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True