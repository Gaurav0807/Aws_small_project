# AWS Lambda S3 Notification Service
AWS Lambda is a compute service that lets you run code without provisioning or managing servers
It is a event-driven architecture.

This AWS Lambda function sends notifications when objects are created or deleted in an Amazon S3 bucket. Notifications are sent to a specified SNS topic.

## Getting Started

These instructions will guide you through setting up and deploying the Lambda function in your AWS environment.

### Prerequisites

- AWS Account
- Python and Boto3 installed locally for testing

### Configuration

1. **Create an SNS Topic:**
   - In the AWS Management Console, navigate to the Simple Notification Service (SNS) service.
   - Create a new topic and note down the Topic ARN.
   - Create Subscriptions to that Topic ARN. 

2. **Configure Lambda Function:**
   - In the AWS Management Console, navigate to the Lambda service.
   - Create a new Lambda function.
   - Configure the function with the following:
      - Runtime: Python (Choose the appropriate version)
      - Role: Create or choose an existing role with S3 and SNS permissions.
      - Trigger: Add an **S3 trigger**  and configure it for both ObjectCreated and ObjectRemoved events.
   - Set the environment variable `SNS_TOPIC_ARN` with the SNS Topic ARN created in step 1.

### Deploy

1. **Clone the repository:**

   bash
   git clone https://github.com/yourusername/lambda-s3-notification.git
   

2. **Try to run from aws console:**

    Copy aws lambda function code and deploy it.

3. **Upload file to s3 bucket/location**

4. **Soon will get notification based on your subscription**





