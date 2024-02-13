from fastapi import APIRouter, UploadFile, File


router = APIRouter()


@router.post("/handgesture/")
async def upload_file(file: UploadFile = File(...)):
    file_contents = await file.read()
    return {"filename": file.filename}
