import boto3
import os

def lambda_handler(event, context):
    instance_id = event.get("instance_id", os.getenv("DEFAULT_INSTANCE_ID"))
    region = os.getenv("AWS_REGION")

    ec2 = boto3.client("ec2", region_name=region)
    ec2.start_instances(InstanceIds=[instance_id])

    return {
        "message": f"Started EC2 instance {instance_id}"
    }
