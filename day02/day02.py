from typing import Iterable

def get_ranges(sequences: str) -> Iterable[int]:
    """Gives product ids given a range string.
    A range string is like '11-14,23-26' would produce
    11, 12, 13, 14, 23, 24, 25, 26
    """
    for sequence_str in sequences.split(','):
        start_str, end_str = sequence_str.split('-')
        start = int(start_str)
        end = int(end_str) + 1 # End is inclusive.
        for num in range(start, end):
            yield num
