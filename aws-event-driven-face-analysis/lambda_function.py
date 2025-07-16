import boto3
import json
import os
from datetime import datetime

rekognition = boto3.client('rekognition')
dynamodb = boto3.resource('dynamodb')

# Set your DynamoDB table name as an environment variable
TABLE_NAME = os.environ['DYNAMODB_TABLE']
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    # Get the S3 bucket and object key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    print(f"Processing image: s3://{bucket}/{key}")
    
    # Call Rekognition to detect facial features
    response = rekognition.detect_faces(
        Image={'S3Object': {'Bucket': bucket, 'Name': key}},
        Attributes=['ALL']
    )
    
    if not response['FaceDetails']:
        print("No faces detected.")
        return {
            'statusCode': 200,
            'body': json.dumps('No face detected.')
        }
    
    # Process only the first detected face (you can modify for multi-face)
    face = response['FaceDetails'][0]

    # Prepare item for DynamoDB
    item = {
        'ImageID': key,
        'Timestamp': datetime.utcnow().isoformat(),
        'AgeRange': f"{face['AgeRange']['Low']}-{face['AgeRange']['High']}",
        'Gender': face['Gender']['Value'],
        'Smile': face['Smile']['Value'],
        'Eyeglasses': face['Eyeglasses']['Value'],
        'Sunglasses': face['Sunglasses']['Value'],
        'Beard': face['Beard']['Value'],
        'Mustache': face['Mustache']['Value'],
        'EyesOpen': face['EyesOpen']['Value'],
        'MouthOpen': face['MouthOpen']['Value'],
        'Emotions': sorted(face['Emotions'], key=lambda e: e['Confidence'], reverse=True)[0]['Type']
    }

    # Store to DynamoDB
    table.put_item(Item=item)

    print("Analysis saved to DynamoDB.")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Facial analysis complete and saved.')
    }
