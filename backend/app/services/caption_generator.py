# import json
# import os
# from pathlib import Path

# from dotenv import load_dotenv
# from openai import OpenAI

# from app.schemas.caption import CaptionResponse

# load_dotenv()

# client = OpenAI(
#     api_key=os.getenv("FIREWORKS_API_KEY"),
#     base_url=os.getenv("FIREWORKS_BASE_URL"),
# )

# MODEL = os.getenv("GEMMA_MODEL")

# PROMPT_PATH = Path("app/prompts/caption_prompt.txt")


# def load_prompt() -> str:
#     with open(PROMPT_PATH, "r", encoding="utf-8") as file:
#         return file.read()


# def generate_captions(transcript: str) -> CaptionResponse:

#     prompt = load_prompt()

#     response = client.chat.completions.create(
#         model=MODEL,
#         messages=[
#             {
#                 "role": "system",
#                 "content": prompt,
#             },
#             {
#                 "role": "user",
#                 "content": f"""
# Transcript:

# {transcript}

# Generate the captions.
# """,
#             },
#         ],
#         temperature=0.7,
#         max_tokens=500,
#         response_format={"type": "json_object"},
#     )

#     captions = json.loads(response.choices[0].message.content)

#     return CaptionResponse(
#         formal=captions["formal"],
#         sarcastic=captions["sarcastic"],
#         humorous_tech=captions["humorous_tech"],
#         humorous_non_tech=captions["humorous_non_tech"],
#     )

import json
import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

from app.schemas.caption import CaptionResponse

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

MODEL = os.getenv("GEMINI_MODEL")

PROMPT_PATH = Path("app/prompts/caption_prompt.txt")


def load_prompt() -> str:
    with open(PROMPT_PATH, "r", encoding="utf-8") as file:
        return file.read()


def generate_captions(transcript: str) -> CaptionResponse:

    prompt = load_prompt()

    full_prompt = f"""
{prompt}

Transcript:

{transcript}
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=full_prompt,
    )

    text = response.text.strip()

    # Remove markdown fences if Gemini returns them
    text = text.replace("```json", "").replace("```", "").strip()

    captions = json.loads(text)

    return CaptionResponse(
        formal=captions["formal"],
        sarcastic=captions["sarcastic"],
        humorous_tech=captions["humorous_tech"],
        humorous_non_tech=captions["humorous_non_tech"],
    )