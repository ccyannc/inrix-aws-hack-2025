import boto3
import os

# --- AWS CONFIG ---
AWS_ACCESS_KEY_ID = "AKIA5EOQSV5VI4IEKW4X"
AWS_SECRET_ACCESS_KEY = "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"
AWS_REGION = "us-east-1"
S3_BUCKET = "lung-xray-uploads"
# ------------------

def upload_file_to_s3(local_path, filename):
    try:
        # Initialize S3 client
        s3 = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_REGION
        )

        # Upload the file
        s3.upload_file(local_path, S3_BUCKET, filename)

        # Construct a public URL (if your bucket allows public access)
        public_url = f"https://{S3_BUCKET}.s3.{AWS_REGION}.amazonaws.com/{filename}"

        print(f"✅ Upload successful! File available at: {public_url}")
        return True, public_url

    except Exception as e:
        print("❌ Upload error:", e)
        return False, None