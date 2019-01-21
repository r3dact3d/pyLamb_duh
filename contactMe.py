import boto3
import json
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    RECEIVER = 'brady.thompson@gmail.com'
    SENDER = 'brady.thompson@gmail.com'
    SUBJECT = 'Website Referral Form: ' + event['name'],
    BODY_HTML = """<html>
        <head></head>
        <body>
        <h1>Amazon SES Test (SDK for Python)</h1>
        <p>This email was sent with
            <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
            <a href='https://aws.amazon.com/sdk-for-python/'>
            AWS SDK for Python (Boto)</a>.</p>
        </body>
        </html>
            """
    BODY_TEXT = 'name: ' + event['name'] + '\nemail: ' + event['email'] + '\nmessage: ' + event['message']
    client = boto3.client('ses')
    CHARSET = 'UTF-8'
    # Try to send the email.
    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination = {
                'ToAddresses': [
                    RECEIVER,
                ],
            },
            Message = {
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source = SENDER,
            # If you are not using a configuration set, comment or delete the
            # following line
            #ConfigurationSetName=CONFIGURATION_SET,
        )
    # Display an error if something goes wrong. 
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])

 
