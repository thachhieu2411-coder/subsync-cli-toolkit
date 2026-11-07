import re
from datetime import datetime, timedelta

TIME_FORMAT = "%H:%M:%S,%f"

def parse_time(time_str):
    time_str = str(time_str).strip()
    if "," not in time_str:
        time_str += ",000"
    return datetime.strptime(time_str, TIME_FORMAT)

def format_time(dt_obj):
    return dt_obj.strftime(TIME_FORMAT)[:-3]

def shift_time(time_str, offset_ms):
    dt = parse_time(time_str)
    shifted = dt + timedelta(milliseconds=offset_ms)
    min_time = datetime.strptime("00:00:00,000", TIME_FORMAT)
    if shifted < min_time:
        shifted = min_time
    return format_time(shifted)

def normalize_subtitle_text(text):
    if not text:
        return ""
    cleaned = re.sub(r"<[^>]*>", "", text)
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in cleaned.split("\n")]
    return "\n".join([line for line in lines if line]).strip()

def fix_overlapping_timestamps(cues):
    fixed_count = 0
    for i in range(len(cues) - 1):
        prev_cue = cues[i]
        curr_cue = cues[i + 1]

        prev_end_str = getattr(prev_cue, "end_time", None)
        curr_start_str = getattr(curr_cue, "start_time", None)

        if prev_end_str and curr_start_str:
            prev_end = parse_time(prev_end_str)
            curr_start = parse_time(curr_start_str)

            if prev_end > curr_start:
                prev_cue.end_time = curr_start_str
                fixed_count += 1

    return fixed_count
