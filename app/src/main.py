from fastapi import FastAPI
from src.api.routes import router as api_router
import uvicorn

app = FastAPI(
    title="Prima SRE Tech Challenge API",
    version="1.0.0",
    description="API to manage users in DynamoDB",
    contact={"name": "Elias Ahiadu", "email": "nxwrth40@gmail.com"},
    docs_url="/docs",
    redoc_url="/redoc"
)

# Root endpoint
@app.get("/")
def root():
    return {"status": "ok", "message": "Welcome to Prima SRE API"}

# Health check
@app.get("/health")
def health_check():
    return {"status": "ok"}

# Dummy users for testing
@app.get("/users")
def get_users():
    dummy_users = [
        {"id": 1, "name": "Elly", "email": "ellyqweku@gmail.com"},
        {"id": 2, "name": "Sam", "email": "sam_george@gmail.com"},
        {"id": 3, "name": "Franklin", "email": "frankkyei@gmail.com"},
    ]
    return dummy_users

# API routes
app.include_router(api_router, prefix="")

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True, log_level="info")
