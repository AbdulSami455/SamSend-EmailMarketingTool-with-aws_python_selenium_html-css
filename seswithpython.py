import boto3

ses =boto3.client('ses', region_name='eu-north-1')
response=ses.list_verified_email_addresses()
print(response)


#Create Template for Email
def createtemplate(name,subject,body,html=None):
 response2 = ses.create_template(
    Template={
        'TemplateName': name,
        'SubjectPart': subject,
        'TextPart': body,
        'HtmlPart': html
    })
 print(response2)


#Listing ALl Templates
def list_templates():
 response=ses.list_templates()
 return response



#Send Email Function
def sendemail(sourc,dest,subject,body):

#Sending Email
 response22=ses.send_email(
    Source=sourc,
    Destination={
        'ToAddresses': [
            dest,
        ],
        'CcAddresses': [
            dest,
        ],
    },
    Message={
        'Subject': {
            'Data': subject,
            'Charset': 'utf-8'
        },
        'Body': {
            'Text': {
                'Data': body,
                'Charset': 'utf-8'
            }
        }
    })


#Update Template
def update_template(templatename,updatedsubject,updatedtextbody):

 response2 = ses.update_template(
    Template={
        'TemplateName': templatename,
        'SubjectPart': updatedsubject,
        'TextPart': updatedtextbody,

    })
 print(response2)


#Send Email with TemplateSend a message

def sendtemplatedemail(templatename):

 response = ses.send_templated_email(
    Source='as1987137@gmail.com',
    Destination={
        'ToAddresses': [
            'msami.bese22seecs@seecs.edu.pk',
        ],
        'CcAddresses': [
            'msami.bese22seecs@seecs.edu.pk',
        ],
    },
    Template=templatename,  # Use the template name
    TemplateData='{}',  # You can provide template data if your template expects variables
      )
 #print(response)