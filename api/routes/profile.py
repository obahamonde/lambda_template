"""
Profile endpoints for the API.
"""

from typing import Dict,Any
from fastapi import APIRouter, Depends, HTTPException, status
from prisma.models import Profile
from api.services.db import db
from api.services.auth import user_with_token


profile = APIRouter()

@profile.post("/profile", response_model=Profile)
async def ep_profile_info_post(payload:Dict[str,Any], user:Dict[str,str] = Depends(user_with_token)):
    """
    Creates a new profile
    """

    
    try:
        return await Profile.prisma().create(data={
            "sub": user["sub"],
            "skills": payload["skills"],
            "jobs": payload["jobs"],
            "education": payload["education"],
            "theme": payload["theme"],
            "bio": payload["bio"],
            "location": payload["location"] if "location" in payload else None,
            "email": user["email"],
            "name": user["name"],
            "picture": user["picture"]
        })
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=exc) from exc