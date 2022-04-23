import boto3
from botocore.exceptions import ClientError

from settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, BUCKET_NAME


class UploadS3Adapter:
    aws_access_key_id = AWS_ACCESS_KEY_ID
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY
    bucket = BUCKET_NAME

    def upload_file(self, file, file_name=None):
        """
        Upload a file to an S3 bucket
        :param file: File to upload
        :param file_name: File name
        :return: File url if file was uploaded, else None
        """
        s3_client = boto3.client(
            's3',
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
        )
        file_name = file_name or file.filename
        try:
            s3_client.upload_fileobj(file, self.bucket, file_name)
        except ClientError:
            return None
        return f'https://s3.amazonaws.com/{self.bucket}/{file_name}'
