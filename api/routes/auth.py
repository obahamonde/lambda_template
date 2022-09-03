"""This is the Auth route module for the API"""
from typing import Any, Dict
from fastapi import APIRouter, HTTPException, status, Depends, BackgroundTasks
from prisma.models import User
from api.services.auth import user_info
from api.models.schemas import User as UserSchema
from api.services.db import db

auth = APIRouter()

@auth.get("/authorize")
async def ep_user_info(user=Depends(user_info)):
    """Entry point"""
    return user

@auth.get("/login")
async def ep_user_register(background_tasks:BackgroundTasks,user:Any= Depends(user_info))->User:
    """Registers user in database"""
    background_tasks.add_task(UserSchema(**user).save)
    try:
        response = await User.prisma().find_unique(where={"sub": user['sub']})
        if response:
            return response
        else:
            response = await User.prisma().create(data=user)
            return response
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc)) from exc