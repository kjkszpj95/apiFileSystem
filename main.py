import os
from fastapi import Depends, FastAPI, UploadFile, File
from fastapi.responses import FileResponse

app = FastAPI()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
