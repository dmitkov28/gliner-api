import boto3
import requests
from requests_aws4auth import AWS4Auth

# AWS credentials
session = boto3.Session()
credentials = session.get_credentials()
region = "eu-central-1"  # e.g., 'us-east-1'

# AWS4Auth for signing requests
awsauth = AWS4Auth(
    credentials.access_key,
    credentials.secret_key,
    region,
    "sagemaker",
    session_token=credentials.token,
)

# SageMaker Endpoint URL
endpoint_name = "gliner-api-endpoint"
url = f"https://runtime.sagemaker.{region}.amazonaws.com/endpoints/{endpoint_name}/invocations"


payload = {
    "keywords": [
        "nike v adidas",
        "nike j guard sizing",
        "nike fc",
        "who stocks nike",
        "nike i watch",
        "nike d'tack 60",
        "nike gt cut academy",
        "nike by you",
        "nike n 354 squash type",
        "nike shox nz",
        "nike with white socks",
        "nike for tennis",
    ],
    "labels": ["sports", "entertainment", "product", "technology", "event"],
}

# Send request
headers = {"Content-Type": "application/json"}
response = requests.post(url, auth=awsauth, json=payload, headers=headers)

# Display response
print(response.status_code)
print(response.json())
