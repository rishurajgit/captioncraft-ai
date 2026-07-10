from pydantic import BaseModel


class CaptionResponse(BaseModel):
    formal: str
    sarcastic: str
    humorous_tech: str
    humorous_non_tech: str