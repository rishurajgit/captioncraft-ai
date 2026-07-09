from fastapi import APIRouter

router = APIRouter(
    prefix="/api/upload",
    tags=["Video Upload"]
)


@router.get("/")
async def upload_status():
    return {
        "message": "Upload API Working 🚀"
    }