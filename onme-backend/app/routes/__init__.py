# Import routers for registration in the main app
from .receipts import router as receipts_router
from .payments import router as payments_router
from .users import router as users_router

# Expose all routers in this package
__all__ = ["receipts_router", "payments_router", "users_router"]
