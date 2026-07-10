# from pathlib import Path

# from app.services.audio import extract_audio
# # from app.services.frame_extractor import extract_frames
# from app.services.metadata import extract_video_metadata
# from app.services.whisper import transcribe_audio

# # from app.services.gemma import analyze_first_frame

# def process_video(video_path: Path):
#     """
#     Process uploaded video.
#     """

#     metadata = extract_video_metadata(video_path)

#     # frames = extract_frames(video_path)
    
#     # print("Frames object:", frames)
#     # print("Output directory:", frames.output_directory)
    
#     # vision = analyze_first_frame(frames.output_directory)

#     audio_path = extract_audio(video_path)
    
#     transcript = transcribe_audio(audio_path)

#     return {
#         "metadata": metadata,
#         # "frames": frames,
#         # "vision": vision,
#         "audio": {
#             "audio_path": audio_path
#         },
#         "transcript": transcript
#     }


from pathlib import Path

from app.services.audio import extract_audio
from app.services.caption_generator import generate_captions
from app.services.metadata import extract_video_metadata
from app.services.whisper import transcribe_audio


def process_video(video_path: Path):
    """
    Process uploaded video.
    """

    metadata = extract_video_metadata(video_path)

    audio_path = extract_audio(video_path)

    transcript = transcribe_audio(audio_path)

    captions = generate_captions(
        transcript.transcript
    )

    return {
        "metadata": metadata,
        "audio": {
            "audio_path": audio_path
        },
        "transcript": transcript,
        "captions": captions
    }