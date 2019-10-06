import os
import boto3


dynamo = boto3.client("dynamodb")


def create_person_table():
    response = dynamo.create_table(
        AttributeDefinitions=[
            {"AttributeName": "person_id", "AttributeType": "S"},
            {"AttributeName": "date_of_birth", "AttributeType": "S"},
            {"AttributeName": "gov_id", "AttributeType": "S"},
            {"AttributeName": "name", "AttributeType": "N"},
        ],
        BillingMode="PAY_PER_REQUEST",
        KeySchema=[{"AttributeName": "person_id", "KeyType": "HASH"}],
        SSESpecification={
            "Enabled": True,
            "SSEType": "AES256",  # "KMS" should be used in all production circumstances
            # "KMSMasterKeyId": "",  # Used in production circumstances to further lock down the database
        },
        TableName=os.getenv("PERSON_TABLE"),
        Tags=[
            {"Key": "Project", "Value": "pseudonym"},
            {"Key": "Contact", "Value": os.getenv("MAINTAINER")},
            {
                "Key": "Purpose",
                "Value": "Store data for tokenized person identifier information",
            },
        ],
    )

    return response


if __name__ == "__main__":
    print(create_person_table())
