from fastapi import FastAPI

app = FastAPI(
    title="CaptionCraft AI",
    description="AI-powered multi-style video caption generator",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "CaptionCraft AI Backend Running 🚀"
    }