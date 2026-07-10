import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types

from app.schemas.vision import VisionResponse

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODEL = os.getenv("GEMINI_MODEL")

PROMPT_PATH = Path("app/prompts/vision_prompt.txt")


def load_prompt() -> str:
    with open(PROMPT_PATH, "r", encoding="utf-8") as file:
        return file.read()


def analyze_frames(frame_directory: str) -> VisionResponse:

    frame_dir = Path(frame_directory)

    images = sorted(frame_dir.glob("*.jpg"))

    if not images:
        raise FileNotFoundError("No extracted frames found.")

    # Select at most 5 evenly spaced frames
    if len(images) > 5:
        step = len(images) // 5
        images = images[::step][:5]

    contents = [load_prompt()]

    for image in images:
        contents.append(
            types.Part.from_bytes(
                data=image.read_bytes(),
                mime_type="image/jpeg",
            )
        )

    response = client.models.generate_content(
        model=MODEL,
        contents=contents,
    )

    return VisionResponse(
        description=response.text
    )