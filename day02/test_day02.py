import unittest

from day02 import get_ranges

class TestDay2(unittest.TestCase):
    def test_range(self):
        ranges = [
            ('11-14,23-26', [11, 12, 13, 14, 23, 24, 25, 26]),
        ]
        for sequence_str, expected_list in ranges:
            with self.subTest(sequence_str=sequence_str):
                result_list = list(get_ranges(sequence_str))
                self.assertListEqual(result_list, expected_list)