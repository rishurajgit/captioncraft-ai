from pydantic import BaseModel


class TranscriptResponse(BaseModel):
    transcript: str
    transcript_path: str