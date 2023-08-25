import boto3

dynamodb=boto3.client('dynamodb', region_name='eu-north-1')

#Create Table on DynamoDb
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


#Enter Data in DynamoDb
def enterData(tablename,templatename,subject,body,html):
 dynamodb.get_waiter('table_exists').wait(TableName=tablename)

 # Insert data into the table
 template_data = [
    {
        'TemplateName': templatename,
        'Subject': subject,
        'Body': body,
        'Html': html
    }]

 for item in template_data:
    dynamodb.put_item(
        TableName=tablename,
        Item={
            'TemplateName': {'S': item['TemplateName']},
            'Subject': {'S': item['Subject']},
            'Body': {'S': item['Body']}
        } )

 print('Data inserted into the table.')


#Fetch Template Data
def fetch_template_data(tablename, templatename):
    response = dynamodb.get_item(
        TableName=tablename,
        Key={
            'TemplateName': {'S': templatename}
        },
        ProjectionExpression='Subject, Body, Html'
    )

    item = response.get('Item')
    if item:
        return {
            'Subject': item['Subject']['S'],
            'Body': item['Body']['S'],

        }
    else:
        return None


table_name = 'EmailTemplates'
template_name = 'Template2'

template_data = fetch_template_data(table_name, template_name)

if template_data:
    print("Subject:", template_data['Subject'])
    print("Body:", template_data['Body'])

else:
    print("Template not found.")