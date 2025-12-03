from textwrap import dedent
import unittest

def prepare(s):
    lines = s.split('\n')
    lines = [line for line in lines if line]
    result = '\n'.join(lines)
    return dedent(result)

class TestBankSelect(unittest.TestCase):
    def test_select(self):
        banks = prepare("""
        987654321111111
        811111111111119
        234234234234278
        818181911112111
        """)
        #print(f'{banks=}')
    
    def test_selections(self):
        scenarios = [
            #(bank, selection)
            ('987654321111111', 98),
            ('811111111111119', 89),
            ('818181911112111', 92),
        ]
        for bank, expected_selection in scenarios:
            with self.subTest(bank=bank):
                selection = select_from_bank(bank)
                self.assertEqual(selection, expected_selection)
