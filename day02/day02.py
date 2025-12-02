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


def id_is_valid(id: int) -> bool:
    """Checks if an id is valid. It is invalid if it is made of repetitions.
    For example, 123 is fine. 11 is not, 1212 is not, 123123 is not.
    :returns: True if the id is valid, False if it is invalid.
    """
    id_str = str(id)
    id_len = len(id_str)
    for check_len in range(1, len(id_str) // 2 + 1):
        check_part = id_str[:check_len]
        repeats = id_len // check_len
        repeated = int(check_part * repeats) # This repeats like 12 * 2 = 1212
        #print(f'{id=} {id_str=} {id_len=} {check_len=} {check_part=} {repeats=} {repeated=}')
        if repeated == id:
            return False
    return True


def find_invalid_ids(range_str: str) -> Iterable[int]:
    return filter(lambda x: not id_is_valid(x), get_ranges(range_str))


def sum_invalid_ids(range_str: str) -> int:
    return sum(find_invalid_ids(range_str))


def main():
    with open('day2_input.txt', 'r') as f:
        line = f.read()
        sequences = line.strip()
    sum_of_invalid = sum_invalid_ids(sequences)
    print(f'{sum_of_invalid=}')


if __name__ == '__main__':
    main()