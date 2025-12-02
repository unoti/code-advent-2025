import unittest

from day02 import get_ranges, id_is_valid, find_invalid_ids, sum_invalid_ids

class TestDay2(unittest.TestCase):
    def test_range(self):
        ranges = [
            ('11-14,23-26', [11, 12, 13, 14, 23, 24, 25, 26]),
        ]
        for sequence_str, expected_list in ranges:
            with self.subTest(sequence_str=sequence_str):
                result_list = list(get_ranges(sequence_str))
                self.assertListEqual(result_list, expected_list)

    def test_detector(self):
        cases = [
            # (id, isValid)
            (55, False),
            (6464, False),
            (123123, False),
            (11, False),
            (1010, False),
            (1234, True),
        ]
        for num, expected_is_valid in cases:
            with self.subTest(num=num):
                is_valid = id_is_valid(num)
                self.assertEqual(is_valid, expected_is_valid)

    def test_find_invalid_ids(self):
        invalid_ids = list(find_invalid_ids('10-24'))
        self.assertListEqual(invalid_ids, [11, 22])

    def test_sum(self):
        self.assertEqual(33, sum_invalid_ids('10-24'))
