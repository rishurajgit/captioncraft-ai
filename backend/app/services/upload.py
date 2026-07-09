from pathlib import Path
from fastapi import UploadFile
from app.services.video_pipeline import process_video


UPLOAD_DIR = Path("uploads/videos")


async def save_video(file: UploadFile) -> dict:
    """
    Save uploaded video to uploads directory.
    """

    UPLOAD_DIR.mkdir(exist_ok=True)

    file_path = UPLOAD_DIR / file.filename

    content = await file.read()

    with open(file_path, "wb") as f:
        f.write(content)
        result = process_video(file_path)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(content),
        "message": "Video uploaded successfully",
        **result
        
    }