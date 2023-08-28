import boto3

s3=boto3.client('s3', region_name='eu-north-1')

response = s3.get_object(Bucket='emailtemplates007', Key='eventinvitation.txt')

# Read the content of the object
object_content = response['Body'].read().decode('utf-8')

# Print or manipulate the content as needed
print(object_content)
subject, body = object_content.split("===")

# Print the subject and body
print("Subject:", subject.strip())  # Remove leading/trailing whitespace
print("\nBody:", body.strip())      # Remove leading/trailing whitespace