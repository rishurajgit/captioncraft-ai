import json
import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

from app.schemas.caption import CaptionResponse
from app.schemas.evaluation import (
    CaptionEvaluation,
    EvaluationResponse,
)

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

MODEL = os.getenv("GEMINI_MODEL")

PROMPT_PATH = Path("app/prompts/evaluation_prompt.txt")


def load_prompt():

    with open(PROMPT_PATH, "r", encoding="utf-8") as file:
        return file.read()


def evaluate_captions(
    captions: CaptionResponse,
) -> EvaluationResponse:

    prompt = load_prompt()

    response = client.models.generate_content(
        model=MODEL,
        contents=f"""
{prompt}

Captions:

Formal:
{captions.formal}

Sarcastic:
{captions.sarcastic}

Humorous Tech:
{captions.humorous_tech}

Humorous Non Tech:
{captions.humorous_non_tech}
""",
    )

    text = response.text.strip()

    text = (
        text.replace("```json", "")
        .replace("```", "")
        .strip()
    )

    result = json.loads(text)

    return EvaluationResponse(
        formal=CaptionEvaluation(**result["formal"]),
        sarcastic=CaptionEvaluation(**result["sarcastic"]),
        humorous_tech=CaptionEvaluation(**result["humorous_tech"]),
        humorous_non_tech=CaptionEvaluation(**result["humorous_non_tech"]),
        recommended_style=result["recommended_style"],
    )