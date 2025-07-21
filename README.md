# AutoInfraBuddy

AI-Powered Infrastructure Automation Agent  
A smart assistant that monitors, automates, and predicts AWS infrastructure operations using GPT, Lambda, PostgreSQL, Dynatrace, and CDK.

---

## Project Overview

AutoInfraBuddy is a lightweight cloud automation agent that performs real-time EC2 health checks, logs infrastructure metrics, and routes natural language commands to AWS operations. The system is built using AWS Lambda, CDK, Boto3, and OpenAI GPT integration, with infrastructure metrics ingested from Dynatrace and logged into PostgreSQL for analysis.

---

## Core Features

- EC2 health monitoring via Lambda and Boto3
- Natural language to infrastructure command routing using GPT-3.5
- Metric ingestion from Dynatrace API
- Logging and storage of CPU usage data into PostgreSQL
- Deployed with AWS CDK using Python
- Real-world simulation with CloudWatch logging and alerting support

--

## Technologies Used

- AWS Lambda, EC2, IAM, CDK (Python)
- OpenAI GPT-3.5 API
- Dynatrace Metrics API
- PostgreSQL (local, for now)
- Python (psycopg2, requests, unittest, etc.)
- GitHub (CI/CD and code history)

---

## Example Use Cases

- Check EC2 instance status with natural language
- Start an EC2 instance based on GPT-tagged commands
- Log CPU usage data into a structured database
- Schedule health checks and simulate real infrastructure operations

---

## How to Run

1. Clone the repo and install dependencies.
2. Deploy infrastructure with AWS CDK:
