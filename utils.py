import re
from datetime import datetime, timedelta

TIME_FORMAT = "%H:%M:%S,%f"

def parse_time(time_str):
    return datetime.strptime(time_str.strip(), TIME_FORMAT)

def format_time(dt_obj):
    return dt_obj.strftime(TIME_FORMAT)[:-3]

def shift_time(time_str, offset_seconds):
    dt = parse_time(time_str)
    shifted = dt + timedelta(seconds=offset_seconds)
    if shifted < datetime.strptime("00:00:00,000", TIME_FORMAT):
        shifted = datetime.strptime("00:00:00,000", TIME_FORMAT)
    return format_time(shifted)

def normalize_subtitle_text(text):
    text = re.sub(r"<[^>]*>", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def fix_overlapping_timestamps(cues):
    fixed_cues = []
    for i in range(len(cues)):
        current = dict(cues[i])
        if i > 0:
            prev_end = parse_time(fixed_cues[i - 1]["end"])
            curr_start = parse_time(current["start"])
            if curr_start < prev_end:
                current["start"] = format_time(prev_end + timedelta(milliseconds=50))
                curr_end = parse_time(current["end"])
                if parse_time(current["start"]) >= curr_end:
                    current["end"] = format_time(parse_time(current["start"]) + timedelta(milliseconds=500))
        fixed_cues.append(current)
    return fixed_cues
