
from fastapi import FastAPI

from app.api.endpoints import login, users

app = FastAPI(
    title="Secure FastAPI Service",
    description="A professional and secure API service for user authentication.",
    version="1.0.0"
)

# Include the routers
app.include_router(login.router, tags=["Login"])
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/", tags=["Root"])
async def read_root():
    """
    A simple root endpoint to confirm the API is running.
    """
    return {"status": "ok", "message": "Welcome to the Secure FastAPI Service!"}