

#def filecreate(params=None, file: UploadFile = File(None)):
@app.post("/filecreate")
async def filecreate(request: FileCreate = Depends(),file: UploadFile = File(None)):
    params = request.paf
    if params:
        folder_path = os.path.join(r"C:\Users\1\PycharmProjects\FileStorage\filestor", params)
        if os.path.exists(folder_path):
            if file:


                with open(os.path.join(folder_path, file.filename), "wb") as f:
                    f.write(file.file.read())
                    file_system = os.listdir(folder_path)
                return {"file_system": file_system , "Ответ": "Файл успешно сохранен"}
            file_system = os.listdir(folder_path)
            return {"file_system": file_system}
        else:
            return "Такого пути не существует"
    else:
        folder_path = r"C:\Users\1\PycharmProjects\FileStorage\filestor"
        if os.path.exists(folder_path):
            if file:
                with open(os.path.join(folder_path, file.filename), "wb") as f:
                    f.write(file.file.read())
                file_system = os.listdir(folder_path)
                return {"file_system": file_system}
            else:
                file_system = os.listdir(folder_path)
                return {"file_system": file_system}
        else:
            return "Такого пути не существует"


@app.post("/download")
async def download(request: DownloadRequest):
    file_name = request.file_name
    paf = request.paf
    if paf:
        folder_path = os.path.join(r"C:\Users\1\PycharmProjects\FileStorage\filestor", paf)
    else:
        folder_path = os.path.join(r"C:\Users\1\PycharmProjects\FileStorage\filestor")

    file_path=os.path.join(folder_path,file_name)

    if os.path.exists(file_path):
        return FileResponse(file_path, filename=file_name)
    else:
        return "Файл не найден"
