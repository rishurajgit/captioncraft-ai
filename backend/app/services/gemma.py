import base64
import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

from app.schemas.vision import VisionResponse

load_dotenv()

client = OpenAI(
    api_key=os.getenv("FIREWORKS_API_KEY"),
    base_url=os.getenv("FIREWORKS_BASE_URL"),
)

MODEL = os.getenv("GEMMA_MODEL")

PROMPT_PATH = Path("app/prompts/vision_prompt.txt")

def load_prompt() -> str:
    with open(PROMPT_PATH, "r", encoding="utf-8") as file:
        return file.read()


def encode_image(image_path: str):
    with open(image_path, "rb") as image:
        return base64.b64encode(image.read()).decode("utf-8")


def analyze_frame(image_path: str):
    
    prompt = load_prompt()

    image_base64 = encode_image(image_path)

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt,
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_base64}"
                        },
                    },
                ],
            }
        ],
        temperature=0.2,
        max_tokens=500,
    )

    return response.choices[0].message.content

def analyze_first_frame(frame_directory: str) -> VisionResponse:
    
    frame_dir = Path(frame_directory)

    images = sorted(frame_dir.glob("*.jpg"))

    if not images:
        raise FileNotFoundError("No extracted frames found.")

    description = analyze_frame(str(images[0]))

    return VisionResponse(
        description=description
    )