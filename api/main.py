"""
Main Module
"""
from typing import Dict
from fastapi import FastAPI, Request
from starlette.templating import Jinja2Templates, _TemplateResponse as TemplateResponse
from starlette.middleware.cors import CORSMiddleware
from api.routes import router
from api.core.search import search_engine
from api.services.db import db


templates = Jinja2Templates(directory="api/templates")

app = FastAPI(title="OB API",
              description="Oscar Bahamonde's API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await db.connect()
    
@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()



app.include_router(router)


@app.get("/")
async def root(root_request: Request) -> TemplateResponse:
    """App root"""
    return templates.TemplateResponse("index.html", {"request": root_request})


@app.get("/api/search/{lang}/{query}/{page}")
async def ep_search(query: str, page: int, lang: str) -> Dict[str, str]:
    """Search Engine Endpoint"""
    return await search_engine(query=query, page=page, lang=lang)
