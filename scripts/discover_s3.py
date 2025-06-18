import boto3, requests, json

# Configuration
AWS_S3 = boto3.client('s3')
ATLAS_BASE = "http://<atlas-host>:21000/api/atlas/v2"
ATLAS_AUTH = ('admin', 'admin')

def list_buckets():
    return [b['Name'] for b in AWS_S3.list_buckets()['Buckets']]

def register_s3_bucket(bucket_name):
    payload = {
        "entity": {
          "typeName": "aws_s3_bucket",
          "attributes": {
            "name": bucket_name,
            "qualifiedName": f"{bucket_name}@aws",
            "owner": "data-governance-team"
          }
        }
    }
    resp = requests.post(f"{ATLAS_BASE}/entity", auth=ATLAS_AUTH,
                         headers={"Content-Type":"application/json"},
                         data=json.dumps(payload))
    resp.raise_for_status()

if __name__ == "__main__":
    for bucket in list_buckets():
        register_s3_bucket(bucket)
        print(f"Registered S3 bucket: {bucket}")