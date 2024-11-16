from pydantic import BaseModel
from typing import List, Dict

class Receipt(BaseModel):
    user_id: str
    image_url: str
    parsed_data: Dict
    created_at: str
