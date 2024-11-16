from fastapi import APIRouter, UploadFile, HTTPException
from ..utils.gpt import extract_text_from_image
import os

router = APIRouter()

@router.post("/test-ocr")
async def test_ocr(file: UploadFile):
    """
    Endpoint to test the OCR functionality using PaddleOCR.

    Args:
        file (UploadFile): The uploaded image file.

    Returns:
        dict: Extracted text from the image.
    """
    try:
        # Save the uploaded file temporarily
        temp_dir = os.path.join(os.getcwd(), "temp")
        os.makedirs(temp_dir, exist_ok=True)
        temp_file_path = os.path.join(temp_dir, file.filename)

        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(await file.read())

        # Use the OCR function to extract text
        extracted_text = extract_text_from_image(temp_file_path)

        # Clean up the temporary file
        # os.remove(temp_file_path)

        return {"extracted_text": extracted_text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
