import boto3
import os

from dotenv import load_dotenv

load_dotenv()

# Put your AWS credentials in a .env file
access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
bucket_name = os.getenv("S3_BUCKET")
aws_region = os.getenv("AWS_REGION")

# ------------------

def upload_file_to_s3(local_path, filename):
    try:
        # Initialize S3 client
        s3 = boto3.client(
            's3',
            aws_access_key_id=access_key_id,
            aws_secret_access_key=secret_access_key,
            region_name=aws_region
        )


        print("DEBUG values:")
        print("local_path =", type(local_path), local_path)
        print("bucket_name =", bucket_name)
        print("filename =", filename)
        # Upload the file
        s3.upload_file(local_path, bucket_name, filename)

        # Construct a public URL (if your bucket allows public access)
        public_url = f"https://{bucket_name}.s3.{aws_region}.amazonaws.com/{filename}"

        print(f"✅ Upload successful! File available at: {public_url}")
        return True, public_url

    except Exception as e:
        print("❌ Upload error:", e)
        return False, None