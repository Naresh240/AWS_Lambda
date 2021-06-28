import boto3
import csv
import json

s3client=boto3.client('s3')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    # print(bucket)
    csv_file = event['Records'][0]['s3']['object']['key']
    response = s3client.get_object(Bucket=bucket, Key=csv_file)
    lines = response['Body'].read().decode('utf-8').split()
    results = []
    for row in csv.DictReader(lines):
        results.append(row.values())
    print(results)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
