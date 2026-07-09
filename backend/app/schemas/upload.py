from pydantic import BaseModel

from app.schemas.video_metadata import VideoMetadata
from app.schemas.frame_extraction import FrameExtractionResponse


class UploadResponse(BaseModel):
    filename: str
    content_type: str
    size: int
    message: str
    metadata: VideoMetadata
    frames: FrameExtractionResponse