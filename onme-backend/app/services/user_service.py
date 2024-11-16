from ..utils.firebase import get_document, update_document


def get_user(user_id: str) -> dict:
    """
    Retrieve user details from Firestore by user ID.
    """
    return get_document("Users", user_id)


def update_user(user_id: str, updates: dict) -> str:
    """
    Update user data in Firestore.
    """
    return update_document("Users", user_id, updates)
