import shutil
from fastapi import FastAPI, UploadFile
import extracttext as ext
import ner as ent

app = FastAPI()


@app.post("/upload_file/")
async def take_file(file: UploadFile):

    with open(file.filename, "wb") as f:
        shutil.copyfileobj(file.file, f)

    text = ext.text_extract(file.filename)
    di = ent.return_entity(text)

    return {"file_name": file.filename, "request": di}
