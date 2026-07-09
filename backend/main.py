from fastapi import FastAPI

from app.api.upload import router as upload_router

app = FastAPI(
    title="CaptionCraft AI",
    description="AI-powered multi-style video caption generator",
    version="1.0.0",
)

app.include_router(upload_router)


@app.get("/")
async def root():
    return {
        "status": "running",
        "project": "CaptionCraft AI",
        "message": "Backend is running successfully 🚀"
    }