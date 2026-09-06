from fastapi import FastAPI, UploadFile, File,HTTPException
from fastapi.staticfiles import StaticFiles
import os
import shutil

app = FastAPI()

#step1 : Ensure uploads folder exist
UPLPAD_DIR = "upload"
if not os.path.exists(UPLPAD_DIR):
    os.makedirs(UPLPAD_DIR)

#step 2: Static file setup
# http://124.0.0.1:8080/Files/<file name>
app.mount("/files",StaticFiles(directory=UPLPAD_DIR),name="files")

#step 3: upload api
@app.post("/upload")
def upload_file(file:UploadFile=File(...) ):
    filename = file.filename
    file_path = os.path.join(UPLPAD_DIR,filename)

    if not filename:
         raise HTTPException(status_code=400, detail="file not selected")
    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        return {
            "message":"File Uploaded",
            "fileName":filename,
            "fileurl":f"http://124.0.0.1:8080/Files/{filename}"
        }
@app.get("files/{filename}")
def get_file(filename:str):
    file_path = os.path.join(UPLPAD_DIR,filename)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=400, detail="file not found")
    return {
        "file_url":f"http://124.0.0.1:8080/Files/{filename}"
    }

@app.get("/")
def home():
    return {
        "message":"file uploaded reunning"
    }
    