from pydantic import BaseModel

from app.schemas.video_metadata import VideoMetadata



class UploadResponse(BaseModel):
    filename: str
    content_type: str
    size: int
    message: str
    metadata: VideoMetadata
    metadata: VideoMetadata