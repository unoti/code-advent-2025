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
    def get_instruction(self) -> Optional[str]:
        ...

