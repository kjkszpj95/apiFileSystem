@app.post("/dircreate")
async def filestor(request: DirectCreate):
    paf = request.paf
    folder_name = request.folder_name
    if paf:
        folder_path = os.path.join(r"C:\Users\1\PycharmProjects\FileStorage\filestor", paf, folder_name)
    else:
        folder_path = os.path.join(r"C:\Users\1\PycharmProjects\FileStorage\filestor", folder_name)

    try:
        os.mkdir(folder_path)
        print(f"Папка {folder_path} успешно создана.")
        return "Папка успешно создана"
    except FileExistsError:
        print(f"Папка {folder_path} уже существует.")
        return "Папка уже существует"

@app.get("/")
async def index(paf=None):
    if paf:
        folder_path = os.path.join(r"C:\Users\1\PycharmProjects\FileStorage\filestor", paf)
    else:
        folder_path = os.path.join(r"C:\Users\1\PycharmProjects\FileStorage\filestor")

    file_system = os.listdir(folder_path)
    return file_system


@app.post("/dirupdate")
async def dirupdate(old_name:str, new_name:str , paf=None):
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
            return {"file_system": file_system, "Ответ": "Папка переименнована"}
        else:
            return "Такого файла не существует"
    else:
        return "Системе не удается найти путь"
