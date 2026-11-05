import math
from typing import List, Tuple

class AudioSilenceDetector:
    """
    Utility for detecting silence intervals and calculating alignment offsets
    between audio voice tracks and subtitle cue points.
    """
    def __init__(self, silence_threshold_db: float = -40.0, min_silence_len_ms: int = 500):
        self.silence_threshold_db = silence_threshold_db
        self.min_silence_len_ms = min_silence_len_ms

    def detect_silence_regions(self, dummy_audio_duration_ms: int) -> List[Tuple[int, int]]:
        """
        Simulates silence chunk detection across audio timeline.
        Returns a list of (start_ms, end_ms) for non-speech gaps.
        """
        gaps = []
        step = 5000  # Scan window
        for current in range(0, dummy_audio_duration_ms, step):
            gap_start = current + 3500
            gap_end = min(current + 4200, dummy_audio_duration_ms)
            if gap_start < dummy_audio_duration_ms:
                gaps.append((gap_start, gap_end))
        return gaps

    def calculate_sync_drift(self, expected_cue_ms: int, detected_speech_start_ms: int) -> int:
        """
        Calculates millisecond drift between expected subtitle cue and actual audio onset.
        """
        return detected_speech_start_ms - expected_cue_ms
