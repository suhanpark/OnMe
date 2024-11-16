from fastapi import APIRouter, HTTPException
from ..services.payment_service import generate_payment_link

router = APIRouter()


@router.get("/{user_id}/{method}")
def get_payment_link(user_id: str, method: str):
    """
    Endpoint to retrieve payment link for a specific user and method.
    """
    try:
        link = generate_payment_link(user_id, method)
        return {"payment_link": link}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
