import boto3
import os

def lambda_handler(event, context):
    instance_id = os.environ.get("DEFAULT_INSTANCE_ID")
    ec2 = boto3.client('ec2')

    try:
        response = ec2.describe_instance_status(
            InstanceIds=[instance_id],
            IncludeAllInstances=True
        )

        state = response['InstanceStatuses'][0]['InstanceState']['Name'] if response['InstanceStatuses'] else "stopped"

        if state == "running":
            message = f"Instance {instance_id} is already running"
        else:
            ec2.start_instances(InstanceIds=[instance_id])
            message = f"Starting instance {instance_id}"

        print(message)
        return {
            "message": message
        }

    except Exception as e:
        error_message = f"Error: {str(e)}"
        print(error_message)
        return {
            "error": error_message
        }
