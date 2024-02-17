import json
import boto3
from botocore.exceptions import ClientError

def send_notification(subject, message):

    sns_topic_arn = "arn:aws:sns:us-east-1:510989898124:gr_test"
    
    sns = boto3.client('sns')
    
    try:
        sns.publish(
            TopicArn=sns_topic_arn,
            Message=message,
            Subject=subject
        )
        print("Notification sent successfully.")
    except ClientError as e:
        print(f"Error sending notification: {e}")

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    

    if 'ObjectCreated' in event['Records'][0]['eventName']:
        send_notification("S3 Object Created", f"New object created in {bucket}: {key}")

    elif 'ObjectRemoved' in event['Records'][0]['eventName']:
        send_notification("S3 Object Deleted", f"Object deleted in {bucket}: {key}")
    else:
        print("Unsupported S3 event type.")