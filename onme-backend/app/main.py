from fastapi import FastAPI
from .routes import receipts_router, payments_router, users_router

app = FastAPI()

# Register routers
app.include_router(receipts_router, prefix="/receipts", tags=["Receipts"])
app.include_router(payments_router, prefix="/payments", tags=["Payments"])
app.include_router(users_router, prefix="/users", tags=["Users"])

@app.get("/")
def root():
    return {"message": "Welcome to OnMe API"}
