from pydantic import BaseModel

class User(BaseModel):
    user_id: str
    name: str
    email: str
    venmo_link: str
    zelle_link: str
    paypal_link: str
