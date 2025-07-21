from lambda_utils import invoke_check_ec2_lambda

INSTANCE_ID = "i-04101e533932e9ccd"

result = invoke_check_ec2_lambda(INSTANCE_ID)
print("EC2 Status:", result)

if "stopped" in result.get("status", "").lower():
    print("GPT Response: EC2 instance is stopped. Consider starting it if required.")
elif "running" in result.get("status", "").lower():
    print("GPT Response: EC2 instance is running normally.")
elif "impaired" in result.get("status", "").lower():
    print("GPT Response: EC2 instance has issues (status impaired). Check CloudWatch or take action.")
else:
    print("GPT Response: EC2 status is unclear or not returned. Further investigation needed.")
