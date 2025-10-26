import boto3, json

def predict_from_sagemaker(image_path, endpoint_name="effusion-cnn-endpoint", region="us-east-1"):
    """
    Sends an image to the deployed SageMaker endpoint and returns the prediction result.
    """
    runtime = boto3.client("sagemaker-runtime", region_name=region)

    with open(image_path, "rb") as f:
        payload = f.read()

    response = runtime.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType="application/x-image",
        Body=payload,
    )

    result = json.loads(response["Body"].read().decode())
    return result