import unittest

from day1 import Safe, InputProvider

class MockInputProvider(InputProvider):
    ...

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


if __name__ == '__main__':
    unittest.main()
