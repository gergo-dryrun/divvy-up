import json


def lambda_handler(event, context):
    print(json.dumps(event))
    print('Hello World')
    if event['path'] == '/upload':
        resp = {
            "isBase64Encoded": False,
            "statusCode": '200',
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({'Status': 'Allez gut.'})
        }
    elif event['path'] == '/download':
        resp = {
            "isBase64Encoded": False,
            "statusCode": '301',
            "headers": {"Location": "https://www.google.com"},
            "body": json.dumps({'Status': 'Allez gut.'})
        }
    return resp
