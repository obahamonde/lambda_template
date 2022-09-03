from pydantic import HttpUrl, EmailStr, Field
from typing import Optional, Union, Any, List, Dict
from api.services.fauna import FQLModel as Q
from api.core.utils import get_avatar, get_id


class User(Q):
    """User Fauna Model"""
    sub: str = Field(...)
    given_name: Optional[str] = Field()
    family_name: Optional[str] = Field()
    nickname: Optional[str] = Field()
    name: Optional[str] = Field()
    picture: Optional[Union[HttpUrl, str]] = Field(default_factory=get_avatar)
    locale: Optional[Union[str, None]] = Field()
    updated_at: Optional[str] = Field()
    email: Union[EmailStr, str, None] = Field(index=True)
    email_verified: Optional[Union[bool, str]] = Field()

