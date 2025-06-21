
from fastapi import FastAPI

app = FastAPI(title="Secure FastAPI Service", version="0.1.0")

@app.get("/", tags=["Root"])
async def read_root():
    """A simple root endpoint to confirm the API is running."""
    return {"message": "Welcome to the Secure FastAPI Service!"}