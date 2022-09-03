"""Email Ngage Module."""
from typing import List, Dict, Any
from pydantic import EmailStr
from botocore.exceptions import ClientError, BotoCoreError
from api.config import session, AWS_SES_MAIL_FROM

async def verify_email(email: EmailStr) -> bool:
    """
    Verify if an email is valid
    """
    async with session.client('ses') as client:
        try:
            response = await client.verify_email_identity(EmailAddress=email)
            if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                return True
            else:
                return False
        except (ClientError, BotoCoreError) as exc:
            raise exc

async def send_email(recipients:List[EmailStr], subject:str, body:str,sender:Any=AWS_SES_MAIL_FROM) -> bool:
    """Send and Email whether from a verified email address or default MAIL_FROM"""
    async with session.client('ses') as client:
        try:
            response = await client.send_email(
                Source=sender,
                Destination={
                    'ToAddresses': recipients
                },
                Message={
                    'Subject': {
                        'Data': subject,
                        'Charset': 'UTF-8'
                    },
                    'Body': {
                        'Text': {
                            'Data': body,
                            'Charset': 'UTF-8'
                        }
                    }
                }
            )
            if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                return True
            else:
                return False
        except (ClientError, BotoCoreError) as exc:
            raise exc