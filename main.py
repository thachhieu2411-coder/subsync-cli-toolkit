import os
import re
import sys
import argparse
from datetime import datetime, timedelta

class SubtitleBlock:
    def __init__(self, index, start_time, end_time, text):
        self.index = int(index)
        self.start_time = start_time
        self.end_time = end_time
        self.text = text.strip()

    def to_srt_format(self):
        return f"{self.index}\n{self.start_time} --> {self.end_time}\n{self.text}\n"

class SRTProcessor:
     TIME_FORMAT = "%H:%M:%S,%f"

    def __init__(self, filepath):
        self.filepath = filepath
        self.blocks = []

    def load(self):
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"Subtitle file not found: {self.filepath}")

        with open(self.filepath, "r", encoding="utf-8") as f:
            content = f.read()

        pattern = re.compile(
            r"(\d+)\s*\n(\d{2}:\d{2}:\d{2},\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2},\d{3})\s*\n((?:.+\n?)+)"
        )
        matches = pattern.findall(content)
        for match in matches:
            self.blocks.append(SubtitleBlock(match[0], match[1], match[2], match[3]))
        print(f"[INFO] Loaded {len(self.blocks)} subtitle blocks from {self.filepath}")

    @staticmethod
    def _parse_time(time_str):
        return datetime.strptime(time_str, SRTProcessor.TIME_FORMAT)

    @staticmethod
    def _format_time(dt_obj):
        return dt_obj.strftime("%H:%M:%S,%f")[:-3]

    def shift_timestamps(self, offset_ms):
        delta = timedelta(milliseconds=offset_ms)
        for block in self.blocks:
            start_dt = self._parse_time(block.start_time) + delta
            end_dt = self._parse_time(block.end_time) + delta
            block.start_time = self._format_time(start_dt)
            block.end_time = self._format_time(end_dt)
        print(f"[INFO] Applied timestamp shift of {offset_ms}ms across all blocks.")

    def save(self, output_path):
        with open(output_path, "w", encoding="utf-8") as f:
            for block in self.blocks:
                f.write(block.to_srt_format() + "\n")
        print(f"[SUCCESS] Saved synchronized subtitles to {output_path}")

def main():
    parser = argparse.ArgumentParser(
        description="SubSync CLI Toolkit - Automated SRT timestamp synchronization utility."
    )
    parser.add_argument("-i", "--input", required=True, help="Path to input .srt file")
    parser.add_argument("-o", "--output", required=True, help="Path to output .srt file")
    parser.add_argument(
        "-s", "--shift", type=int, default=0, help="Shift timestamps in milliseconds (e.g., 500 or -300)"
    )

    args = parser.parse_args()
    processor = SRTProcessor(args.input)
    processor.load()

    if args.shift != 0:
        processor.shift_timestamps(args.shift)

    processor.save(args.output)

if __name__ == "__main__":
    main()
