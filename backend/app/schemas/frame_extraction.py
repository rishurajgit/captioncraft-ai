from pydantic import BaseModel


class FrameExtractionResponse(BaseModel):
    total_frames: int
    extracted_frames: int
    output_directory: str