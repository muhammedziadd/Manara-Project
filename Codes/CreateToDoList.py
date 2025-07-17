import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ToDoList-Table')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        todo_id = str(uuid.uuid4())
        task = body['task']
        created_at = datetime.utcnow().isoformat()

        item = {
            'id': todo_id,
            'task': task,
            'created_at': created_at
        }

        table.put_item(Item=item)

        return {
            'statusCode': 201,
            'body': json.dumps({'message': 'Task created successfully', 'id': todo_id})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
