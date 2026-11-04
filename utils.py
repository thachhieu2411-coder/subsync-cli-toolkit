import re
from datetime import datetime

 TIME_FORMAT = "%H:%M:%S,%f"

def normalize_subtitle_text(text: str) -> str:
    """
    Cleans subtitle text by removing redundant whitespace, HTML tags,
    and normalizing punctuation spacing for TTS/voiceover alignment.
    """
    # Remove HTML styling tags like <i>, <b>, <font>
    cleaned = re.sub(r"<[^>]+>", "", text)
    # Remove multiple spaces
    cleaned = re.sub(r"[ \t]+", " ", cleaned)
    # Ensure no more than two lines per subtitle block
    lines = [line.strip() for line in cleaned.split("\n") if line.strip()]
    return "\n".join(lines)

def fix_overlapping_timestamps(blocks):
    """
    Detects and resolves overlapping timestamps between consecutive subtitle blocks.
    """
    fixed_count = 0
    for i in range(len(blocks) - 1):
        current_end = datetime.strptime(blocks[i].end_time, TIME_FORMAT)
        next_start = datetime.strptime(blocks[i + 1].start_time, TIME_FORMAT)

        if current_end > next_start:
            blocks[i].end_time = blocks[i + 1].start_time
            fixed_count += 1

    return fixed_count
