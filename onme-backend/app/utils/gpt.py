import requests

OPENAI_API_KEY = "your_openai_api_key"


def process_receipt_with_gpt(ocr_text: str) -> dict:
    """
    Use OpenAI GPT API to extract structured data from OCR text.
    """
    headers = {"Authorization": f"Bearer {OPENAI_API_KEY}"}
    payload = {
        "prompt": f"Extract items and total from the following receipt text:\n{ocr_text}",
        "model": "text-davinci-003",
        "max_tokens": 500,
    }
    response = requests.post("https://api.openai.com/v1/completions", json=payload, headers=headers)
    response.raise_for_status()
    return response.json()["choices"][0]["text"]
