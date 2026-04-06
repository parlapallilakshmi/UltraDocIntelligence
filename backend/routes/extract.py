from fastapi import APIRouter, HTTPException

from backend.routes.upload import DOCUMENT_TEXT
from backend.services.parser import parse_file
from backend.services.extraction import extract_data

router = APIRouter()



from backend.models.schemas import ExtractRequest

@router.post("/extract")
async def extract(req: ExtractRequest):

    if not DOCUMENT_TEXT:
        raise HTTPException(status_code=400, detail="No document uploaded")

    return extract_data(DOCUMENT_TEXT)
    #text = parse_file(req.file_path)
    #return extract_data(text)
