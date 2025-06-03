import boto3

client = boto3.client('dynamodb', region_name='eu-west-1')

response = client.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'pk',
            'AttributeType': 'S',
        },
        {
            'AttributeName': 'sk',
            'AttributeType': 'S',
        },
    ],
    KeySchema=[
        {
            'AttributeName': 'pk',
            'KeyType': 'HASH', #partition key
        },
        {
            'AttributeName': 'sk',
            'KeyType': 'RANGE', #soft key
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5,
    },
    TableName='tech-world',
)

print(response)