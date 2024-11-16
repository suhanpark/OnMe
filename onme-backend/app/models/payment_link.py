from pydantic import BaseModel

class PaymentLink(BaseModel):
    user_id: str
    method: str
    link: str
