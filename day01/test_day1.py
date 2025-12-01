import unittest
from typing import List

from day1 import Safe, InputProvider, SafeOperator, FileInputProvider

class MockInputProvider(InputProvider):
    def __init__(self, instructions: List[str]):
        self.instructions = instructions
    
    def get_instruction(self):
        if not self.instructions:
            return None
        instruction = self.instructions[0]
        self.instructions = self.instructions[1:]
        return instruction

class TestSafe(unittest.TestCase):
    def setUp(self):
        self.safe = Safe()

    def test_start(self):
        self.assertEqual(self.safe.number, 50)

    def test_left(self):
        self.safe.apply_instruction("L1")
        self.assertEqual(self.safe.number, 49)

    def test_right(self):
        self.safe.apply_instruction("R2")
        self.assertEqual(self.safe.number, 52)

    def test_roll_left(self):
        self.safe.apply_instruction("L51")
        self.assertEqual(self.safe.number, 99)

    def test_roll_right(self):
        self.safe.apply_instruction("R51")
        self.assertEqual(self.safe.number, 1)

    # Tests from the instructions
    def test_start5(self):
        self.safe.number = 5
        self.safe.apply_instruction("L10")
        self.assertEqual(self.safe.number, 95)
        self.safe.apply_instruction("R5")
        self.assertEqual(self.safe.number, 0)

    def test_example_doc(self):
        example_instructions = [
            'L68',
            'L30',
            'R48',
            'L5',
            'R60',
            'L55',
            'L1',
            'L99',
            'R14',
            'L82',
        ]
        expected_positions = [50, 82, 52, 0, 95, 55, 0, 99, 0, 14, 32]

        input_provider = MockInputProvider(example_instructions)
        safe_operator = SafeOperator(self.safe, input_provider)
        zero_count = safe_operator.run()
        self.assertEqual(zero_count, 3)


class TestInput(unittest.TestCase):
    def test_input(self):
        provider = FileInputProvider('day1_input.txt')
        all_instructions = []
        while True:
            instruction = provider.get_instruction()
            if not instruction:
                break
            all_instructions.append(instruction)
        ins1 = all_instructions[0]
        self.assertEqual(ins1, "R45")

        last_instruction = all_instructions[-1]
        self.assertEqual(last_instruction, 'R48')

        self.assertEqual(len(all_instructions), 4424)

if __name__ == '__main__':
    unittest.main()
