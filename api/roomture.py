import os

from fastapi import APIRouter
from starlette.responses import JSONResponse
from fastapi.responses import FileResponse
from models.models import DirectCreate
from models.models import FileCreate, DownloadRequest
from dirsync import sync

router = APIRouter()


@router.get("/room")
async def index(paf=None):
    if paf:
        folder_path = os.path.join(r"\\DESKTOP-C31KK4F\Users\User\Documents\public\roomtour", paf)
    else:
        folder_path = os.path.join(r"\\DESKTOP-C31KK4F\Users\User\Documents\public\roomtour")

    file_system = os.listdir(folder_path)
    return file_system


@router.post("/download_room")
async def download(request: DownloadRequest):
    file_name = request.file_name
    paf = request.paf
    if paf:
        folder_path = os.path.join(r"\\DESKTOP-C31KK4F\Users\User\Documents\public\roomtour", paf)
    else:
        folder_path = os.path.join(r"\\DESKTOP-C31KK4F\Users\User\Documents\public\roomtour")

    file_path = os.path.join(folder_path, file_name)

    if os.path.exists(file_path):
        return FileResponse(file_path, filename=file_name)
    else:
        return JSONResponse(content={"message": "Такого файла не существует"}, status_code=404)


@router.get("/syncs")
async def syncs():
    source_path = r'\\DESKTOP-C31KK4F\Users\User\Documents\public\roomtour'
    target_path = r'C:\Users\1\PycharmProjects\FileStorage\filestor\roomtour'
    sync(source_path, target_path, 'sync', purge=True)  # for syncing one way
    # sync(target_path, source_path, 'sync')  # for syncing the opposite way



