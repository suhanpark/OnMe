from fastapi import APIRouter, HTTPException, UploadFile, Form
from ..services.receipt_service import process_receipt

router = APIRouter()


@router.post("/")
async def create_receipt(file: UploadFile, user_id: str = Form(...)):
    """
    Endpoint to upload and process a receipt image.
    """
    try:
        # Save uploaded file locally
        file_path = f"./temp/{file.filename}"
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        # Process the receipt
        result = process_receipt(file_path, user_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
