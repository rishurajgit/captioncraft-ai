from fastapi import FastAPI

from app.api.upload import router as upload_router

from fastapi.middleware.cors  import CORSMiddleware


app = FastAPI(
    title="CaptionCraft AI",
    description="AI-powered multi-style video caption generator",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    
)


app.include_router(upload_router)


@app.get("/")
async def root():
    return {
        "status": "running",
        "project": "CaptionCraft AI",
        "message": "Backend is running successfully"
    }