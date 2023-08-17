import os

from fastapi.responses import FileResponse
from fastapi import Depends, UploadFile, File, APIRouter
from starlette.responses import JSONResponse

from models.models import FileCreate, DownloadRequest

router = APIRouter()


# def filecreate(params=None, file: UploadFile = File(None)):
@router.post("/filecreate")
async def filecreate(request: FileCreate = Depends(), file: UploadFile = File(None)):
    params = request.paf
    if params:
        folder_path = os.path.join(r"C:\Users\1\PycharmProjects\FileStorage\filestor", params)
        if os.path.exists(folder_path):
            if file:
                with open(os.path.join(folder_path, file.filename), "wb") as f:
                    f.write(file.file.read())
                    file_system = os.listdir(folder_path)
                return JSONResponse(content={"message": "Файл успешно сохранен"}, status_code=200)
            file_system = os.listdir(folder_path)
            return JSONResponse(content={"message": "Файл не передан"}, status_code=404)
        else:
            os.makedirs(folder_path)
            if file:
                with open(os.path.join(folder_path, file.filename), "wb") as f:
                    f.write(file.file.read())
                    file_system = os.listdir(folder_path)
                return JSONResponse(content={"message": "Файл успешно сохранен"}, status_code=200)
            file_system = os.listdir(folder_path)
            return JSONResponse(content={"message": "Файл не передан"}, status_code=404)

    else:
        folder_path = r"C:\Users\1\PycharmProjects\FileStorage\filestor"
        if os.path.exists(folder_path):
            if file:
                with open(os.path.join(folder_path, file.filename), "wb") as f:
                    f.write(file.file.read())
                file_system = os.listdir(folder_path)
                return JSONResponse(content={"message": "Файл успешно сохранен"}, status_code=200)
            else:
                file_system = os.listdir(folder_path)
                return JSONResponse(content={"message": "Файл не передан"}, status_code=404)
        else:
            return JSONResponse(content={"message": "Пути не существует"}, status_code=404)


@router.post("/download")
async def download(request: DownloadRequest):
    file_name = request.file_name
    paf = request.paf
    if paf:
        folder_path = os.path.join(r"C:\Users\1\PycharmProjects\FileStorage\filestor", paf)
    else:
        folder_path = os.path.join(r"C:\Users\1\PycharmProjects\FileStorage\filestor")

    file_path = os.path.join(folder_path, file_name)

    if os.path.exists(file_path):
        return FileResponse(file_path, filename=file_name)
    else:
        return JSONResponse(content={"message": "Такого файла не существует"}, status_code=404)


@router.post("/delete")
async def delete(request: DownloadRequest):
    file_name = request.file_name
    paf = request.paf
    if paf:
        folder_path = os.path.join(r"C:\Users\1\PycharmProjects\FileStorage\filestor", paf)
    else:
        folder_path = os.path.join(r"C:\Users\1\PycharmProjects\FileStorage\filestor")

    file_path = os.path.join(folder_path, file_name)

    if os.path.exists(file_path):
        os.remove(file_path)
        return JSONResponse(content={"message": "Файл удален"}, status_code=200)
    else:
        return JSONResponse(content={"message": "Такого файла не существует"}, status_code=404)
