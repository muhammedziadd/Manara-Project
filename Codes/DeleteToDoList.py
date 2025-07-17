import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ToDoList-Table')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        todo_id = body['id']

        response = table.delete_item(
            Key={'id': todo_id}
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Task deleted successfully'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
