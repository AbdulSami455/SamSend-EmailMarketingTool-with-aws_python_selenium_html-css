import boto3

dynamodb=boto3.client('dynamodb', region_name='eu-north-1')


def createtable(tablename):

 table_name = tablename
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

def enterData(tablename,templatename,subject,body,html):
 table_name = tablename

 dynamodb.get_waiter('table_exists').wait(TableName=table_name)

 # Insert data into the table
 template_data = [
    {
        'TemplateName': templatename,
        'Subject': subject,
        'Body': body,
        'Html':html
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


