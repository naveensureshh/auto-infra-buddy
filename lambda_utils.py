import boto3
import json

def invoke_check_ec2_lambda(instance_id):
    client = boto3.client("lambda")

    payload = {
        "instance_id": instance_id
    }

    response = client.invoke(
        FunctionName="AutoInfraCdkStack-CheckEC2StatusFunctionE71EB3A5-4lngvK7mg83V",
        InvocationType="RequestResponse",
        Payload=json.dumps(payload)
    )

    result = json.load(response["Payload"])
    return result
