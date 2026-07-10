from app.services.caption_generator import generate_captions

result = generate_captions(
    """
When you get stuck and don't remember the right word,
instead of staying silent you can use filler phrases.
"""
)

print(result)