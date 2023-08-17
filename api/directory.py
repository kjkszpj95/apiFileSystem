import os

from fastapi import APIRouter
from starlette.responses import JSONResponse

from models.models import DirectCreate

router = APIRouter()


@router.post("/dircreate")
async def filestor(request: DirectCreate):
    paf = request.paf
    folder_name = request.folder_name
    if paf:
        folder_path = os.path.join(r"C:\Users\1\PycharmProjects\FileStorage\filestor", paf, folder_name)
    else:
        folder_path = os.path.join(r"C:\Users\1\PycharmProjects\FileStorage\filestor", folder_name)

    try:
        os.makedirs(folder_path)
        #os.mkdir(folder_path)
        print(f"Папка {folder_path} успешно создана.")
        return JSONResponse(content={"message": "Папка успешно создана"}, status_code=200)
    except FileExistsError:
        print(f"Папка {folder_path} уже существует.")
        return JSONResponse(content={"message": "Папка уже существует"}, status_code=404)


@router.get("/")
async def index(paf=None):
    if paf:
        folder_path = os.path.join(r"C:\Users\1\PycharmProjects\FileStorage\filestor", paf)
    else:
        folder_path = os.path.join(r"C:\Users\1\PycharmProjects\FileStorage\filestor")

    file_system = os.listdir(folder_path)
    return file_system


@router.post("/dirupdate")
async def dirupdate(old_name: str, new_name: str, paf=None):
    if paf:
        folder_path = os.path.join(r"C:\Users\1\PycharmProjects\FileStorage\filestor", paf)
    else:
        folder_path = os.path.join(r"C:\Users\1\PycharmProjects\FileStorage\filestor")
    if os.path.exists(folder_path):
        old_path = os.path.join(folder_path, old_name)
        if os.path.exists(old_path):
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)
            file_system = os.listdir(folder_path)
            return  JSONResponse(content={"message": "Папка переименнована"}, status_code=200)
        else:
            return JSONResponse(content={"message": "Такого файла не существует"}, status_code=404)
    else:
        return JSONResponse(content={"message": "Системе не удается найти путь"}, status_code=404)
