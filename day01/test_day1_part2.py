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

    def test_full_scenario_part2(self):
        """The full example scenario"""
        instructions = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']
        expected_landings = [82, 52, 0, 95, 55, 0, 99, 0, 14, 32]
        expected_zero_crossings = 6
        input_provider = MockInputProvider(instructions)
        operator = SafeOperator2(self.safe, input_provider)
        zero_crossings = operator.run()
        self.assertListEqual(expected_landings, operator.landings)

        self.assertEqual(expected_zero_crossings, zero_crossings)

    def test_multi_scenario_part2(self):
        scenarios = [
            # ([instructions], expected_zero_crossings)
            #(['L51', 'R52'], 2),
            #(['L10', 'R90'], 1),
            #(['L151'], 2),
            #(['R151'], 2),
            #(['R100'], 1),
            #(['R200'], 2),
            #(['R150'], 2),
            #(['R250'], 3),
            #(['L350'], 4),
            #(['R350'], 4), # 3 crossings for the 300, an extra crossing for the 50.
            #(['R50', 'L10'], 1),  # 50 -> 0 (crosses once to zero), 0 -> 90 (stays on same side, no crossing)
            #(['R1', 'L2'], 0), # From 50 -> 51 (0 crosses), from 51 -> 49 (zero)
            #(['R50', 'L150'], 2), # 50->0 (1 cross), 0 to 150 (1 cross) = 2
            (['R50', 'L250'], 3), # 50->0 (1 cross), back to 50 with 2 crosses = 3.
            #(['R100'], 1), # From 50, R100 goes to 50 with 1 cross.
            #(['L50', 'R1'], 1), # 50->0 (1 cross), 0-1 (0 crosses) = 1 cross.
        ]

        for instructions, expected_crossings in scenarios:
            with self.subTest(instructions=instructions, expected_crossings=expected_crossings):
                input_provider = MockInputProvider(instructions)
                safe = Safe2()
                operator = SafeOperator2(safe, input_provider)
                actual_crossings = operator.run()
                self.assertEqual(expected_crossings, actual_crossings)
