from ..utils.firebase import get_document


LINKS = {'venmo': 'https://venmo.com/u/',
         'paypal': 'https://www.paypal.com/paypalme/',
         'zelle': 'https://zelle.com/pay/'}

def generate_payment_link(user_id: str, method: str) -> str:
    """
    Generate a payment link for the specified method (Venmo, PayPal, Zelle).
    """
    user_data = get_document("Users", user_id)

    if not user_data:
        raise ValueError("User not found")

    payment_username = user_data.get(f"{method}")
    if not payment_username:
        raise ValueError(f"No payment link found for method: {method}")
    
    payment_link = LINKS[method] + payment_username
    return payment_link
