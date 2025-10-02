import os
import boto3

dynamodb = boto3.resource("dynamodb", region_name="us-east-1")

def get_table():
    table_name = os.getenv("TABLE_NAME")
    if not table_name:
        raise RuntimeError("TABLE_NAME environment variable not set")
    return dynamodb.Table(table_name)

def put_user(user):
    table = get_table()
    table.put_item(Item=user)

def list_users():
    table = get_table()
    response = table.scan()
    return response.get("Items", [])

