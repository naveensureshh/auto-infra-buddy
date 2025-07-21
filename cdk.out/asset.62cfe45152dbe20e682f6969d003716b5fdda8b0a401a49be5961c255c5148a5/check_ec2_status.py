import boto3
import os

def lambda_handler(event, context):
    instance_id = event.get("instance_id", os.getenv("DEFAULT_INSTANCE_ID"))
    region = os.getenv("AWS_REGION")

    ec2 = boto3.client("ec2", region_name=region)
    response = ec2.describe_instance_status(InstanceIds=[instance_id])

    statuses = response.get("InstanceStatuses", [])
    if statuses:
        result = {
            "instance_id": instance_id,
            "status": statuses[0]["InstanceState"]["Name"]
        }
    else:
        result = {
            "instance_id": instance_id,
            "status": "stopped (no status returned)"
        }

    print(result)
    return result
