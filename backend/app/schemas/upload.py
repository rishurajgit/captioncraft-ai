from pydantic import BaseModel

from app.schemas.video_metadata import VideoMetadata
from app.schemas.frame_extraction import FrameExtractionResponse
from app.schemas.audio import AudioResponse
from app.schemas.transcript import TranscriptResponse

class UploadResponse(BaseModel):
    filename: str
    content_type: str
    size: int
    message: str
    metadata: VideoMetadata
    frames: FrameExtractionResponse
    audio: AudioResponse
    transcript: TranscriptResponse