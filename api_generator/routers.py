from fastapi import APIRouter
from endpoints import home_page, thumbnail_service

router = APIRouter()

router.include_router(home_page.router, tags=["Home"])
router.include_router(thumbnail_service.router, tags=["Thumbnail Generator"])
