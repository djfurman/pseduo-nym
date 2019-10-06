# pseudonym

A micro-tokenization setup for human information using AWS DynamoDB

## Purpose

When storing information about humans, security is critical. This play on words for an alias is a simple micro-tokenization framework. After passing information in, this service is designed to provide a safe meaningless token that can be passed around services and even if exposed will not compromise identifying information.

## Model

### Person

```json
{
    "person": {
        "date_of_birth": "1939-10-27",
        "name": {
            "given": "John",
            "middle": "Marwood",
            "surname": "Cleese",
        },
        "tax_id": "123-45-0000"
    }
}
```

### Address

```json
{
    "address": {
        "street": "49321 Dominic Road",
        "line2": "Apt. 861",
        "city": "North Jennifer",
        "state_code": "WA",
        "postal_code": "99124",
        "latitude": {
            "degrees": 48.0009,
            "direction": "N"
        },
        "longitude": {
            "degrees": 118.9533,
            "direction": "W"
        }
    }
}
```

### Personal Info

```json
{
    "personal_info": {
        "person": "5cc75b5f-2b50-4dcf-8c2c-4344ed257028",
        "addresses": [
            {
                "token": "89ebc048-f57d-4548-8d2a-aaaef9470915",
                "type": "mailing"
            },
            {
                "token": "7916ca8a-cd39-4a91-a4d8-0ef48022f5d2",
                "type": "billing"
            }
        ]
    }
}

```

## Setup

### DynamoDB

Run `aws cloudformation create-stack --stack-name pseudonym --template-url https://djf-pseudonym.s3.amazonaws.com/templates/storage.yml --parameters ParameterKey=Environment,ParameterValue=sandbox ParameterKey=Maintainer,ParameterValue="djfurman@gmail.com" --tags Key=Contact,Value="djfurman@gmail.com" Key=Project,Value=pseudonym Key=Purpose,Value="obfuscate personally identifiable information"`

## Release Notes

### v0.0.1

- Initial Setup using DynamoDB for data storage
- Add CFT file to create DynamoDB table
