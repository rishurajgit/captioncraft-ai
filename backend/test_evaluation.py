from app.schemas.caption import CaptionResponse
from app.services.evaluation_service import evaluate_captions

captions = CaptionResponse(
    formal="Professional caption.",
    sarcastic="Sarcastic caption.",
    humorous_tech="Tech joke caption.",
    humorous_non_tech="Funny caption."
)

result = evaluate_captions(captions)

print(result)