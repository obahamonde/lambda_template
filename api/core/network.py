"""Network Module"""
from typing import Dict, Any, Union
import aiohttp
from pydantic import HttpUrl
from api.config import USER_AGENT

default_headers = {
        "user-agent": USER_AGENT
    }

async def fetch_json(url: Union[HttpUrl,str], headers: Dict[str, Any] = default_headers) -> Dict[str,Any]:
    """Used to fetch APIs"""
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            return await response.json()
        
        
async def fetch_html(url: Union[HttpUrl,str],headers: Dict[str, Any] = default_headers) -> str:
    """Used to fetch HTML"""
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            return await response.text(encoding='utf-8')