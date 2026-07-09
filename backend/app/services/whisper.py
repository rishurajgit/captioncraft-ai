from pathlib import Path

import whisper

from app.schemas.transcript import TranscriptResponse

TRANSCRIPT_DIR = Path("uploads/transcripts")

# Load model only once
model = whisper.load_model("base")


def transcribe_audio(audio_path: str) -> TranscriptResponse:
    """
    Transcribe audio using Whisper.
    """

    TRANSCRIPT_DIR.mkdir(parents=True, exist_ok=True)

    audio_file = Path(audio_path)

    result = model.transcribe(str(audio_file))

    transcript = result["text"]

    transcript_path = TRANSCRIPT_DIR / f"{audio_file.stem}.txt"

    with open(transcript_path, "w", encoding="utf-8") as file:
        file.write(transcript)

    return TranscriptResponse(
        transcript=transcript,
        transcript_path=str(transcript_path),
    )