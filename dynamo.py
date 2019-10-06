import boto3
import os

dynamo = boto3.client('dynamodb')


def add_record(unique_id, record):
    dynamo.put_item(
        TableName=os.getenv("TABLE_NAME"),
        Item={
            unique_id: {
                "M": {
                    "name": {
                        "M": {
                            "given": "S": record["name"]["given"]
                        }
                }
            }
        },
        ReturnValues="None",
    )

    return unique_id
