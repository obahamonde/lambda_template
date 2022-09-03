"""Storage Module"""
from typing import List
from api.config import AWS_S3_BUCKET, session

async def create_file(key:str, body:bytes, content_type:str)->str:
    """Uploads a file to S3"""
    async with session.client('s3') as client:
        await client.put_object(Bucket=AWS_S3_BUCKET, Key=key, Body=body, ContentType=content_type, ACL='public-read')
    return f"https://{AWS_S3_BUCKET}.s3.amazonaws.com/{key}"

async def create_folder(key:str)->str:
    """Creates a folder in S3"""
    async with session.client('s3') as client:
        await client.put_object(Bucket=AWS_S3_BUCKET, Key=key+'/.gitkeep', Body=b'', ContentType='text/plain', ACL='public-read')
    return f"https://{AWS_S3_BUCKET}.s3.amazonaws.com/{key}"

async def delete_folder(key:str)->bool:
    """Deletes a folder in S3"""
    async with session.client('s3') as client:
        response = await client.delete_object(Bucket=AWS_S3_BUCKET, Key=key)
    return response['ResponseMetadata']['HTTPStatusCode'] == 204

async def delete_file(key:str)->bool:
    """Deletes a file in S3"""
    async with session.client('s3') as client:
        response = await client.delete_object(Bucket=AWS_S3_BUCKET, Key=key)
    return response['ResponseMetadata']['HTTPStatusCode'] == 204

async def get_file(key:str)->bytes:
    """Downloads a file from S3"""
    async with session.client('s3') as client:
        response = await client.get_object(Bucket=AWS_S3_BUCKET, Key=key)
    return response['Body'].read()

supported_content_types = ['application', 'audio', 'image', 'text', 'video']

async def list_files(key:str)->List[str]:
    """Lists files in S3"""
    async with session.client('s3') as client:
        response = await client.list_objects_v2(Bucket=AWS_S3_BUCKET, Prefix=key)
    return [obj['Key'] for obj in response['Contents'] if obj['Key'].split('.')[-1] in supported_content_types]

async def list_folders(key:str)->List[str]:
    """Lists folders in S3"""
    async with session.client('s3') as client:
        response = await client.list_objects_v2(Bucket=AWS_S3_BUCKET, Prefix=key)
    return [obj['Key'] for obj in response['CommonPrefixes']]