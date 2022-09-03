from typing import List, Dict
from fastapi import APIRouter, HTTPException, status
from prisma.models import Upload
from api.core.search import search_pypi
from api.core.storage import create_file as upload_file, delete_file, get_file, create_folder, delete_folder, delete_file, get_file, list_files, list_folders


cli  = APIRouter()

@cli.get("/dev/alien/add/{query}")
async def ep_pypi_search(query: str)->List[Dict[str,str]]:
    """Search Engine Endpoint"""
    try:
        return await search_pypi(query=query, page=1)
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    
@cli.get("/dev/alien/search/{query}/{page}")
async def ep_pypi_paginated_search(query: str, page:int=1)->List[Dict[str,str]]:
    """Search Engine Endpoint"""
    try:
        return await search_pypi(query=query, page=page)
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc

@cli.post("/dev/mkdir/{path}")
async def ep_mkdir(path: str)->str:
    """Create Folder Endpoint"""
    try:
        return await create_folder(key=path)
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    
@cli.get("/dev/touch/{path}")
async def ep_touch(path: str)->str:
    """Create File Endpoint"""
    try:
        return await upload_file(key=path, body=b'', content_type='text/plain')
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    
@cli.get("/dev/rm/{path}")
async def ep_rm(path: str)->bool:
    """Delete File Endpoint"""
    try:
        return await delete_file(key=path)
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    
@cli.get("/dev/cat/{path}")
async def ep_cat(path: str)->str:
    """Download File Endpoint"""
    try:
        binary = await get_file(key=path)
        return binary.decode('utf-8')
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    
@cli.get("/dev/ls/{path}")
async def ep_ls(path: str)->List[str]:
    """List Files Endpoint"""
    try:
        return await list_files(key=path)
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc