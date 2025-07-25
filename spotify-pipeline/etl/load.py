import boto3
from pathlib import Path
from botocore.exceptions import NoCredentialsError

BUCKET_NAME = 'spotify-pipeline-akari'
LOCAL_FILE_PATH = Path('data/processed/spotify-2023-cleaned.csv')
S3_KEY = 'cleaned/spotify-2023-cleaned.csv'

def upload_to_s3(local_path: Path, bucket: str, s3_key):
    s3 = boto3.client('s3')

    try:
        s3.upload_file(str(local_path), bucket, s3_key)
        print(f'File uploaded to s3://{bucket}/{s3_key}')

    except FileNotFoundError:
        print(f'File not found at {local_path}')
    except NoCredentialsError:
        print('AWS credentials not found. Run `aws configure`.')

if __name__ == "__main__":
    upload_to_s3(LOCAL_FILE_PATH, BUCKET_NAME, S3_KEY)