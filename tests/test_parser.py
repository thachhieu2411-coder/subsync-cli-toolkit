import unittest
from utils import normalize_subtitle_text, fix_overlapping_timestamps
from main import SubtitleBlock

class TestSubSyncToolkit(unittest.TestCase):
    def test_text_normalization(self):
        raw_text = "<i>Hello   world!</i>\n\nThis is a test.  "
        expected = "Hello world!\nThis is a test."
        self.assertEqual(normalize_subtitle_text(raw_text), expected)

    def test_overlap_fix(self):
        block1 = SubtitleBlock(1, "00:00:01,000", "00:00:04,000", "First line")
        block2 = SubtitleBlock(2, "00:00:03,500", "00:00:06,000", "Second line")
        blocks = [block1, block2]

        fixed_count = fix_overlapping_timestamps(blocks)
        self.assertEqual(fixed_count, 1)
        self.assertEqual(blocks[0].end_time, "00:00:03,500")

if __name__ == "__main__":
    unittest.main()
