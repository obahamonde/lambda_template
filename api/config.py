"""
Env variables
"""
from os import getenv
from dotenv import load_dotenv
import aioboto3

load_dotenv()

AWS_ACCESS_KEY_ID = getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = getenv('AWS_SECRET_ACCESS_KEY')
AWS_DEFAULT_REGION = getenv('AWS_DEFAULT_REGION')
AWS_S3_BUCKET = getenv('AWS_S3_BUCKET')
AWS_SES_MAIL_FROM = getenv('AWS_SES_MAIL_FROM')
AUTH_DOMAIN = getenv('AUTH0_DOMAIN')
USER_AGENT = getenv('USER_AGENT')
FAUNA_SECRET = getenv('FAUNA_SECRET')
session = aioboto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_DEFAULT_REGION
)