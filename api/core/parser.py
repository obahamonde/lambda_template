import re
from pydantic import HttpUrl
from api.core.network import fetch_html


async def get_yt_video_id(url: HttpUrl) -> List
