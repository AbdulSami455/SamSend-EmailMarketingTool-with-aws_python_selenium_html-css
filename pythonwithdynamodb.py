import boto3

dynamodb=boto3.client('dynamodb', region_name='eu-north-1')


def createtable():

 table_name = 'EmailTemplates'
# Create the DynamoDB table
 dynamodb.create_table(
    TableName=table_name,
    KeySchema=[
        {
            'AttributeName': 'TemplateName',
            'KeyType': 'HASH'  # Primary key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'TemplateName',
            'AttributeType': 'S'  # String data type
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    })

 print(dynamodb)

def enterData():
 table_name = 'EmailTemplates'

 dynamodb.get_waiter('table_exists').wait(TableName=table_name)

 # Insert data into the table
 template_data = [
    {
        'TemplateName': 'Template1',
        'Subject': 'Welcome to Our Newsletter',
        'Body': 'Dear {{name}}, welcome to our newsletter...',
        'Html':'____'
    },
    {
        'TemplateName': 'Template2',
        'Subject': 'Important Update',
        'Body': 'Hello, we have an important update for you...',
        'Html':'____'
    }]

 for item in template_data:
    dynamodb.put_item(
        TableName=table_name,
        Item={
            'TemplateName': {'S': item['TemplateName']},
            'Subject': {'S': item['Subject']},
            'Body': {'S': item['Body']}
        } )

 print('Data inserted into the table.')