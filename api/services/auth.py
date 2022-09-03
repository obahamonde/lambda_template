"""Auth Module"""
from typing import Dict
from pydantic import HttpUrl
from fastapi import Request, status, HTTPException
from api.config import AUTH_DOMAIN
from api.core.network import fetch_json


USER_INFO_ENDPOINT = 'https://'+str(AUTH_DOMAIN)+'/userinfo'

async def user_info(req: Request)-> Dict[str,str]:
    """Main dependency"""
    try:
        token =  req.headers.get('Authorization').split(' ')[1]
        return await fetch_json(HttpUrl(scheme="https", url=USER_INFO_ENDPOINT), headers={'Authorization': 'Bearer ' + token})
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc)) from exc
    
async def get_sub(req: Request)-> str:
    """Gets sub to make some operations with it"""
    return (await user_info(req))['sub']

async def user_with_token(token:str)-> Dict[str,str]:
    """Gets user info from token"""
    return await fetch_json(HttpUrl(scheme="https", url=USER_INFO_ENDPOINT), headers={'Authorization': 'Bearer ' + token})