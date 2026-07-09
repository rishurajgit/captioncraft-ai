from pathlib import Path

import cv2

from app.schemas.video_metadata import VideoMetadata


def extract_video_metadata(video_path: Path) -> VideoMetadata:
    """
    Extract metadata from a video using OpenCV.
    """

    cap = cv2.VideoCapture(str(video_path))

    if not cap.isOpened():
        raise ValueError("Unable to open video.")

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    duration = frame_count / fps if fps else 0

    cap.release()

    return VideoMetadata(
        filename=video_path.name,
        fps=round(fps, 2),
        duration=round(duration, 2),
        width=width,
        height=height,
        frame_count=frame_count,
    )