from typing import List
from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks, status
from pydantic import EmailStr
from api.services.auth import user_info
from api.core.email import send_email, verify_email

email = APIRouter()

@email.get('/verify')
async def ep_verify_email(user=Depends(user_info))->bool:
    """Verify if an email is valid"""
    try:
        return await verify_email(user['email'])
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc

@email.post('/send')
async def ep_send_email(recipients: List[EmailStr], subject: str, body: str, user=Depends(user_info))->Dict[str,str]:
    """Send an email"""
    try: 
        response = await send_email(sender=user["email"], recipients=recipients, subject=subject, body=body)
        if response:
            return {"message": "Email sent Successfully"}
        else:
            return {"message": "Failed to send email, verify your credentials"}
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc