from alb_response import alb_response
from http import HTTPStatus


def lambda_handler(event, context):
    return alb_response(
        http_status=HTTPStatus.CREATED,
        json={"token": "5a0dec97-1b4c-44bc-964f-23f7617b6081"},
    )
