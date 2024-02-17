import json

def lambda_handler(event, context):

    print("Hyy Gaurav Lambda Function ")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
