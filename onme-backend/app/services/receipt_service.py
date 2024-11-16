from ..utils.firebase import save_to_firestore
from ..utils.gpt import process_receipt_with_gpt
import pytesseract


def process_receipt(image_path: str, user_id: str) -> dict:
    """
    Handles receipt processing workflow: OCR and structured data extraction.
    """
    # Step 1: Perform OCR on receipt image
    ocr_text = pytesseract.image_to_string(image_path)

    # Step 2: Process OCR text using GPT
    structured_data = process_receipt_with_gpt(ocr_text)

    # Step 3: Save receipt data to Firestore
    receipt_id = save_to_firestore("receipts", {
        "user_id": user_id,
        "ocr_text": ocr_text,
        "parsed_data": structured_data
    })

    return {"receipt_id": receipt_id, "structured_data": structured_data}
