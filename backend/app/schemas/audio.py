from pydantic import BaseModel


class AudioResponse(BaseModel):
    audio_path: str