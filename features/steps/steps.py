from behave import given, when, then
from faker import Faker
import os
import requests
import json

fake = Faker()


class LambdaContext:
    function_name = "tokenize"
    invoked_function_arn = "arn:aws:lambda:us-east-1:123456789012:function:tokenize:stable"
    aws_request_id = fake.uuid()


def alb_lambda_request(body, tokenize=True):
    return {
        "requestContext": {
            "elb": {
                "targetGroupArn": "arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/lambda-function/1283756ef98735a98",
            },
        },
        "httpMethod": "POST",
        "path": "/tokenize" if tokenize else "/detokenize",
        "headers": {"accept": "application/json", "content-type": "application/json"},
        "body": json.dumps(body),
        "isBase64Encoded": False,
    }


def build_payload(context):
    return {
        "person": context.person,
        "address": context.address["address"],
        "tax_id": context.tax_id,
    }


@given(u"a fake person")
def create_a_fake_person(context):
    context.person = {
        "name": {
            "given": fake.first_name(),
            "middle": fake.first_name(),
            "surname": fake.last_name(),
        }
    }


@given(u"a fake address")
def create_a_fake_address(context):
    state_code = fake.state_abbr(include_territories=False)
    context.address = {
        "address": {
            "street": fake.street_address(),
            "line2": fake.secondary_address()
            if fake.boolean(chance_of_getting_true=30)
            else None,
            "city": fake.city(),
            "state_code": state_code,
            "postal_code": fake.postal_code_in_state(state_abbr=state_code),
        }
    }


@given(u"a fake tax ID")
def create_a_fake_tax_id(context):
    context.tax_id = fake.ssn()


@when(u"the value is tokenized")
def call_the_tokenizer(context):
    body = build_payload(context)
    if os.getenv("CALL_LAMBDA") is not None:
        if os.getenv("CALL_LAMBDA").lower() == "true":
            event = alb_lambda_request(body, tokenize=True)

            response = lambda_function.lambda_handler(event, LambdaContext())

            context.response_status_code = response["statusCode"]
            context.response_body = json.loads(response["body"])
            context.response_headers = response["headers"]

    elif os.getenv("SERVICE_URL") is not None:
        response = requests.post(
            os.getenv("SERVICE_URL"),
            headers={"accept": "application/json", "content-type": "application/json"},
            json=context.body,
        )

        context.response_status_code = response.status_code
        context.response_body = response.json()
        context.response_headers = response.headers

    else:
        raise NotImplementedError("tokenization is not implemented")


@then(u"a token should be returned")
def assert_a_token_was_returned(context):
    assert context.response_body["token"] is not None
    assert len(context.response_body["token"]) == 36


@then(u"the information should be stored in the persistance layer")
def assert_information_was_stored(context):
    raise NotImplementedError(
        u"STEP: Then the information should be stored in the persistance layer"
    )


@given(u"a token")
def fetch_a_valid_token(context):
    raise NotImplementedError(u"STEP: Given a token")


@when(u"the value is detokenized")
def call_the_detokenizer(context):
    raise NotImplementedError(u"STEP: When the value is detokenized")


@then(u"it should return the person")
def assert_person_is_returned(context):
    raise NotImplementedError(u"STEP: Then it should return the person")


@then(u"the address")
def assert_address_is_returned(context):
    raise NotImplementedError(u"STEP: Then the address")


@then(u"the tax ID")
def assert_tax_id_is_returned(context):
    raise NotImplementedError(u"STEP: Then the tax ID")
