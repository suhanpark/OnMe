from fastapi import APIRouter, UploadFile, HTTPException
from ..utils.gpt import process_receipt_image
import os

router = APIRouter()

@router.post("/")
async def create_receipt(file: UploadFile):
    """
    Endpoint to upload and process a receipt image.

    Args:
        file: The uploaded receipt image.

    Returns:
        dict: Processed receipt data including extracted JSON details.
    """
    try:
        # Save the uploaded file temporarily
        temp_dir = os.path.join(os.getcwd(), "temp")
        os.makedirs(temp_dir, exist_ok=True)
        temp_file_path = os.path.join(temp_dir, file.filename)

        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(await file.read())

        # Process the receipt image using OCR + GPT
        result = process_receipt_image(temp_file_path)

        # Clean up the temporary file
        # os.remove(temp_file_path)

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
