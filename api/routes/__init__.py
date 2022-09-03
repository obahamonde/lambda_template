"""Router"""
from fastapi import APIRouter
from api.routes.auth import auth
from api.routes.upload import upload
from api.routes.profile import profile
from api.routes.cli import cli

router = APIRouter(prefix="/api")

router.include_router(auth, tags=["auth"])
router.include_router(upload, tags=["upload"])
router.include_router(profile, tags=["profile"])
router.include_router(cli, tags=["cli"])