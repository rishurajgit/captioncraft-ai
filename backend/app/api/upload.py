# from fastapi import APIRouter

# router = APIRouter(
#     prefix="/api/upload",
#     tags=["Video Upload"]
# )


# @router.get("/")
# async def upload_status():
#     return {
#         "message": "Upload API Working "
#     }

from fastapi import APIRouter, File, UploadFile

from app.schemas.upload import UploadResponse
from app.services.upload import save_video

router = APIRouter(
    prefix="/api/upload",
    tags=["Video Upload"]
)


@router.post("/", response_model=UploadResponse)
async def upload_video(
    file: UploadFile = File(...)
):
    return await save_video(file)