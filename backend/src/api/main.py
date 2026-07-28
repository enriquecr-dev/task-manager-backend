from fastapi import FastAPI
from fastapi.responses import JSONResponse

# Initialize the FastAPI application with professional metadata
app = FastAPI(
    title="Task Manager API",
    description="Professional backend for task and team management.",
    version="1.0.0",
    docs_url="/api/docs",  # Custom URL for Swagger documentation
    redoc_url="/api/redoc",
)


# Root endpoint / Health check
@app.get("/api/health", tags=["Health"])
async def health_check() -> JSONResponse:
    """
    Health check endpoint to monitor API status.
    """
    return JSONResponse(
        content={"status": "ok", "message": "Task Manager API is running securely."},
        status_code=200,
    )
