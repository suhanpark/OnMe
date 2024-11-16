from fastapi import APIRouter, HTTPException
from ..services.user_service import get_user, update_user

router = APIRouter()


@router.get("/{user_id}")
def retrieve_user(user_id: str):
    """
    Endpoint to retrieve user details by user ID.
    """
    try:
        user_data = get_user(user_id)
        if not user_data:
            raise HTTPException(status_code=404, detail="User not found")
        return user_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/{user_id}")
def modify_user(user_id: str, updates: dict):
    """
    Endpoint to update user details.
    """
    try:
        update_user(user_id, updates)
        return {"message": "User updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
