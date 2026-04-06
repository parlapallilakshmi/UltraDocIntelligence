from fastapi import APIRouter, UploadFile
import shutil
from backend.services.parser import parse_file
from backend.services.chunking import chunk_text
from backend.dataastore.vector_store import create_vector_store

router = APIRouter()
DOCUMENT_TEXT=""
@router.post("/upload")
async def upload(file: UploadFile):
    global DOCUMENT_TEXT
    path = f"data/uploads/{file.filename}"


    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    text = parse_file(path)
    DOCUMENT_TEXT=text
    if "could not be parsed" in text.lower():
        return {"message": text}
    print("Parsed text length:", len(text))
    chunks = chunk_text(text)

    create_vector_store(chunks)

    return {"message": "Processed"}