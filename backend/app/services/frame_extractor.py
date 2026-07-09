from pathlib import Path

import cv2

from app.schemas.frame_extraction import FrameExtractionResponse


FRAME_DIR = Path("uploads/frames")


def extract_frames(video_path: Path) -> FrameExtractionResponse:
    """
    Extract one frame every second.
    """

    FRAME_DIR.mkdir(parents=True, exist_ok=True)

    video_name = video_path.stem

    output_folder = FRAME_DIR / video_name
    output_folder.mkdir(exist_ok=True)

    cap = cv2.VideoCapture(str(video_path))

    if not cap.isOpened():
        raise ValueError("Unable to open video.")

    fps = int(cap.get(cv2.CAP_PROP_FPS))

    if fps <= 0:
        fps = 30

    frame_count = 0
    saved_count = 0

    while True:

        success, frame = cap.read()

        if not success:
            break

        if frame_count % fps == 0:

            frame_path = output_folder / f"frame_{saved_count:04d}.jpg"

            cv2.imwrite(str(frame_path), frame)

            saved_count += 1

        frame_count += 1

    cap.release()

    return FrameExtractionResponse(
        total_frames=frame_count,
        extracted_frames=saved_count,
        output_directory=str(output_folder),
    )