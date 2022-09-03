"""
Uploads endpoints for the API.
"""
from asyncio import sleep
from typing import Dict, List
from fastapi import APIRouter, HTTPException, status, Depends, UploadFile, File
from prisma.models import Upload
from api.services.auth import user_info
from api.services.db import db
from api.core.storage import create_file as upload_file, delete_file as delete_file, list_files, list_folders, create_folder, delete_folder, get_file
from api.core.utils import get_id

upload = APIRouter()


@upload.post("/upload/{sub}")
async def ep_upload_file(sub: str, key:str="/", file: UploadFile = File(...)) -> Upload:
    """
    Uploads a file to S3.
    """
    key = f"{sub}{key}{file.filename}"
    url = await upload_file(key=key, body=file.file.read(), content_type=file.content_type)
    try:
        return await Upload.prisma().create(data={"url": url, "filename": file.filename, "contentType": file.content_type, "user": {"connect": {"sub": sub}}})
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(exc)) from exc

@upload.get("/upload/{sub}")
async def ep_get_uploads(sub: str) -> List[Upload]:
    """
    Gets all uploads for a user.
    """
    try:
        response = await Upload.prisma().find_many(where={"sub": sub})
        await sleep(2)
        return response
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc)) from exc

   

@upload.get("/upload/delete/{id}")
async def ep_delete_upload(id: str) -> str:
    """
    Deletes an upload.
    """
    try:
        response = await Upload.prisma().delete(where={"id": id})
        return response
        
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc)) from exc


@upload.get("/upload/download/{id}")
async def ep_download_upload(id: str, user: Dict[str, str] = Depends(user_info)) -> bytes:
    """
    Downloads an upload.
    """
    try:
        file = await Upload.prisma().find_unique(where={"id": id})
        if file is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Upload not found")
        if file.sub != user['sub']:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Upload not found")
        return await get_file(file.key)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc)) from exc

@upload.get("/upload/{key}/{filename}")
async def ep_download(key:str, filename:str) ->bytes:
    """
    Downloads an upload.
    """
    try:
        return await get_file(key)
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc)) from exc
