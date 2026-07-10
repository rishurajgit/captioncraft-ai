from pydantic import BaseModel


class CaptionEvaluation(BaseModel):
    caption: str
    score: int
    reason: str


class EvaluationResponse(BaseModel):
    formal: CaptionEvaluation
    sarcastic: CaptionEvaluation
    humorous_tech: CaptionEvaluation
    humorous_non_tech: CaptionEvaluation

    recommended_style: str