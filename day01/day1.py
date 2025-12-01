from abc import ABC, abstractmethod
from typing import Optional

class Safe:
    def __init__(self, starting_number: int = 50):
        self.number = 50
        self.spots = 100

    def apply_instruction(self, instruction: str):
        direction = instruction[0]
        units = int(instruction[1:])
        if direction not in ['L', 'R']:
            raise ValueError(f'Instruction {instruction} is not valid')

        if direction == 'L':
            sign = -1
        else:
            sign = 1
        
        self.number = (self.number + sign * units) % self.spots


class InputProvider(ABC):
    @abstractmethod
    def all_instructions(self) -> Optional[str]:
        """A generator that returns each instruction one at a time."""


class FileInputProvider(InputProvider):
    def __init__(self, filename: str):
        self.filename = filename

    def all_instructions(self):
        with open(self.filename, 'r') as file:
            for line in file.readlines():
                instruction = line.strip()
                yield instruction


class SafeOperator:
    def __init__(self, safe: Safe, input_provider: InputProvider):
        self.safe = safe
        self.input_provider = input_provider
    
    def run(self) -> int:
        """Runs the sequence of operations and returns the number of times we landed on 0."""
        zero_count = 0
        for instruction in self.input_provider.all_instructions():
            if not instruction:
                break
            self.safe.apply_instruction(instruction)
            print(f'Applied {instruction} to point at {self.safe.number}')
            if self.safe.number == 0:
                zero_count += 1

        print(f'Final number {self.safe.number}. Landed on zero {zero_count} times.')
        return zero_count


def main():
    input_provider = FileInputProvider('day1_input.txt')
    safe = Safe()
    operator = SafeOperator(safe, input_provider)
    zero_count = operator.run()
    print(f'Answer: {zero_count}')

if __name__ == '__main__':
    main()