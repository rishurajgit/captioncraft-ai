from pydantic import BaseModel


class VideoMetadata(BaseModel):
    filename: str
    fps: float
    duration: float
    width: int
    height: int
    frame_count: int