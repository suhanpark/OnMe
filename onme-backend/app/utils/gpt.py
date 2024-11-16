import os
from paddleocr import PaddleOCR
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve OpenAI API Key from .env
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("Missing OpenAI API Key. Please set OPENAI_API_KEY in your .env file.")

# Initialize PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang="en")  # You can change the language if needed

def extract_text_from_image(image_path: str) -> str:
    """
    Extract text from an image using PaddleOCR.

    Args:
        image_path (str): Path to the image file.

    Returns:
        str: Extracted text from the image.
    """
    try:
        result = ocr.ocr(image_path, cls=True)
        # Combine detected text into a single string
        extracted_text = "\n".join([line[1][0] for line in result[0]])
        return extracted_text.strip()
    except Exception as e:
        raise ValueError(f"OCR processing failed: {str(e)}")

def process_receipt_with_gpt(ocr_text: str) -> dict:
    """
    Use OpenAI GPT API to process OCR text from the receipt.

    Args:
        ocr_text (str): Text extracted from the receipt via OCR.

    Returns:
        dict: Parsed structured data extracted by GPT.
    """
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a financial assistant. Extract receipt details in JSON format "
                    "including vendor, location, date, time, items, prices, total, tip, and total with tip."
                )
            },
            {
                "role": "user",
                "content": f"Process this receipt and return the information in JSON format:\n\n{ocr_text}"
            }
        ],
        "max_tokens": 500
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", json=payload, headers=headers)

    if response.status_code != 200:
        raise Exception(f"GPT API call failed: {response.status_code} - {response.text}")

    result = response.json()
    structured_data = result.get("choices", [{}])[0].get("message", {}).get("content", "").strip()

    return structured_data

def process_receipt_image(image_path: str) -> dict:
    """
    Full workflow: Extract text from receipt image and process it with GPT.

    Args:
        image_path (str): Path to the receipt image.

    Returns:
        dict: Processed receipt data.
    """
    ocr_text = extract_text_from_image(image_path)  # Step 1: OCR
    structured_data = process_receipt_with_gpt(ocr_text)  # Step 2: GPT
    return structured_data
