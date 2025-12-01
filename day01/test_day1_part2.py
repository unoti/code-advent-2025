import unittest

from test_day1 import MockInputProvider
from day1_part2 import Safe2, SafeOperator2

class TestSafe2(unittest.TestCase):
    def setUp(self):
        self.safe = Safe2()

    def test_zero_cross(self):
        zero_crossings = self.safe.apply_instruction('L68')
        self.assertEqual(zero_crossings, 1)
        self.assertEqual(self.safe.number, 82)

    def test_full_scenario(self):
        """The full example scenario"""
        instructions = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L84']
        expected_landings = [82, 52, 0, 95, 55, 0, 99, 0, 14, 32]
        expected_zero_crossings = 6
        input_provider = MockInputProvider(instructions)
        operator = SafeOperator2(self.safe, input_provider)
        zero_crossings = operator.run()
        self.assertListEqual(expected_landings, operator.landings)
