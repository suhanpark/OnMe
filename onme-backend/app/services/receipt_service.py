from ..utils.firebase import save_to_firestore
from ..utils.gpt import process_receipt_with_gpt
import pytesseract
import os

def process_receipt(image_path: str, user_id: str) -> dict:
    """
    Handles receipt processing workflow: OCR and structured data extraction.
    """
    # Ensure the file exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"File not found at path: {image_path}")

    # Step 1: Perform OCR on receipt image
    try:
        ocr_text = pytesseract.image_to_string(image_path)
    except Exception as e:
        raise ValueError(f"OCR processing failed: {str(e)}")

    # Step 2: Process OCR text using GPT
    try:
        structured_data = process_receipt_with_gpt(ocr_text)
    except Exception as e:
        raise ValueError(f"GPT processing failed: {str(e)}")

    # Step 3: Save receipt data to Firestore
    receipt_id = save_to_firestore("Receipts", {
        "user_id": user_id,
        "ocr_text": ocr_text,
        "parsed_data": structured_data
    })

    return {"receipt_id": receipt_id, "structured_data": structured_data}
