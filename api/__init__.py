from fastapi import APIRouter
from .file import router as file_router
from .directory import router as directory_router


router = APIRouter()
router.include_router(file_router)
router.include_router(directory_router)
