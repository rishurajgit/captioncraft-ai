from pathlib import Path

from app.services.audio import extract_audio
from app.services.frame_extractor import extract_frames
from app.services.metadata import extract_video_metadata
from app.services.whisper import transcribe_audio

def process_video(video_path: Path):
    """
    Process uploaded video.
    """

    metadata = extract_video_metadata(video_path)

    frames = extract_frames(video_path)

    audio_path = extract_audio(video_path)
    
    transcript = transcribe_audio(audio_path)

    return {
        "metadata": metadata,
        "frames": frames,
        "audio": {
            "audio_path": audio_path
        },
        "transcript": transcript
    }