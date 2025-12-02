import argparse
import sys
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
        print(f'sequence {start=} {end=}')
        for num in range(start, end):
            yield num


def id_is_valid_multi(id: int) -> bool:
    """Checks if an id is valid. It is invalid if it is made of repetitions.
    For example, 123 is fine. 11 is not, 1212 is not, 123123 is not.
    This variation detects repeats any number of times, not just twice.
    :returns: True if the id is valid, False if it is invalid.
    """
    id_str = str(id)
    id_len = len(id_str)
    for check_len in range(1, len(id_str) // 2 + 1):
        check_part = id_str[:check_len]
        repeats = id_len // check_len
        repeated = int(check_part * repeats) # This repeats like 12 * 2 = 1212
        if repeated == id:
            return False
    return True


def id_is_valid(id: int) -> bool:
    """Checks if an id is valid. It is invalid if it is made of a string repeated twice.
    For example, 123 is fine. 11 is not, 1212 is not, 123123 is not.
    :returns: True if the id is valid, False if it is invalid.
    """
    id_str = str(id)
    id_len = len(id_str)
    half_len = id_len // 2
    if id_len / 2 != half_len:
        return True
    half = id_str[:half_len]
    repeated = half * 2
    if id_str == repeated:
        return False
    return True


def find_invalid_ids(range_str: str, valid_detector=id_is_valid) -> Iterable[int]:
    return filter(lambda x: not valid_detector(x), get_ranges(range_str))


def sum_invalid_ids(range_str: str, valid_detector=id_is_valid) -> int:
    return sum(find_invalid_ids(range_str, valid_detector=valid_detector))


def dianostics():
    sequences = '194-253,81430782-81451118'
    total = 0
    for id in find_invalid_ids(sequences):
        total += id
        print(f'   {total=} {id=}')
    sum_of_invalid = sum_invalid_ids(sequences)
    print(f'{sum_of_invalid=}')


def get_input():
    with open('day2_input.txt', 'r') as f:
        line = f.read()
        sequences = line.strip()
    return sequences


def main(valid_detector=id_is_valid):
    sum_of_invalid = sum_invalid_ids(get_input(), valid_detector=valid_detector)
    print(f'{sum_of_invalid=}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Advent of Code Day 2: Find invalid product IDs')
    parser.add_argument('--part', type=int, choices=[1, 2], default=1,
                        help='Which part of the challenge to solve (default: 1)')
    args = parser.parse_args()
    
    if args.part == 2:
        main(valid_detector=id_is_valid_multi)
    else:
        main()
