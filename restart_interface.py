import boto3

def restart_instance(instance_id):
    ec2 = boto3.client("ec2")

    try:
        ec2.reboot_instances(InstanceIds=[instance_id])
        print(f"Successfully sent reboot command to {instance_id}")
    except Exception as e:
        print(f"Failed to restart instance: {e}")
