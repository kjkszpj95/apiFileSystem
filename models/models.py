from pydantic import BaseModel


class BasePaf(BaseModel):
    paf: str = None


class DownloadRequest(BasePaf):
    file_name: str


class DirectCreate(BasePaf):
    folder_name: str


class FileCreate(BasePaf):
    pass
