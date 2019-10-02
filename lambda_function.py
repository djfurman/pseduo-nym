import base64
import json
from http import HTTPStatus

from alb_response import alb_response

import dynamo
import person_controller


def lambda_handler(event, context):
    request = fetch_http_request(event)

    person_to_tokenize = person_controller.build_person_store(request)

    token = dynamo.add_record(person_to_tokenize)
    return alb_response(http_status=HTTPStatus.CREATED, json={"token": token})


def fetch_http_request(event):
    if event["isBase64Encoded"]:
        payload = base64.b64decode(event["body"])
    else:
        payload = event["body"]

    if isinstance(payload, bytes):
        body = payload.decode("utf-8")

    return {
        "headers": event["headers"],
        "body": json.loads(body),
        "method": event["httpMethod"],
        "path": event["path"],
    }
