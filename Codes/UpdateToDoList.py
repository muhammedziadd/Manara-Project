import json
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ToDoList-Table')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        todo_id = body['id']
        updated_task = body['task']

        response = table.update_item(
            Key={'id': todo_id},
            UpdateExpression='SET task = :t, updated_at = :u',
            ExpressionAttributeValues={
                ':t': updated_task,
                ':u': datetime.utcnow().isoformat()
            },
            ReturnValues='UPDATED_NEW'
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Task updated successfully', 'updated': response['Attributes']})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
