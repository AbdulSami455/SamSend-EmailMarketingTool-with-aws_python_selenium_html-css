import boto3

ses =boto3.client('ses', region_name='eu-north-1')
response=ses.list_verified_email_addresses()

'''response2 = ses.create_template(
    Template={
        'TemplateName': 'string3',
        'SubjectPart': 'string3',
        'TextPart': 'string3',
        'HtmlPart': 'string3'
    }
)'''

#Listing ALl Templates
response=ses.list_templates()
print(response)

#Sending Email
response22=ses.send_email(
    Source='as1987137@gmail.com',
    Destination={
        'ToAddresses': [
            'msami.bese22seecs@seecs.edu.pk',
        ],
        'CcAddresses': [
            'msami.bese22seecs@seecs.edu.pk',
        ]'Html': {
                'Data': 'string',
                'Charset': 'string'
            }
    },
    Message={
        'Subject': {
            'Data': 'Hello Brother',
            'Charset': 'utf-8'
        },
        'Body': {
            'Text': {
                'Data': 'Hi, Consider My Message ',
                'Charset': 'utf-8'
            }
        }
    }
)