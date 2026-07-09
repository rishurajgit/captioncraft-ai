from pathlib import Path

from moviepy import VideoFileClip


AUDIO_DIR = Path("uploads/audio")


def extract_audio(video_path: Path) -> str:
    """
    Extract audio from video and save as WAV.
    """

    AUDIO_DIR.mkdir(parents=True, exist_ok=True)

    video_name = video_path.stem

    output_path = AUDIO_DIR / f"{video_name}.wav"

    clip = VideoFileClip(str(video_path))

    if clip.audio is None:
        raise ValueError("No audio track found in video.")

    clip.audio.write_audiofile(
        str(output_path),
        logger=None
    )

    clip.close()

    return str(output_path)