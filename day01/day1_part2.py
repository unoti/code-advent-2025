from day1 import InputProvider


class Safe2:
    def __init__(self, starting_number: int = 50):
        self.number = 50
        self.spots = 100

    def apply_instruction(self, instruction: str) -> int:
        """Apply an instruction and return how many times we crossed zero."""
        direction = instruction[0]
        units = int(instruction[1:])
        if direction not in ['L', 'R']:
            raise ValueError(f'Instruction {instruction} is not valid')

        if direction == 'L':
            sign = -1
        else:
            sign = 1

        extra_crossings = abs(units) // self.spots
        new_number = self.number + sign * units
        if new_number < 0 or new_number >= self.spots:
            extra_crossings += 1
        self.number = (self.number + sign * units) % self.spots
        
        total_crossings = extra_crossings
        return total_crossings



class SafeOperator2:
    def __init__(self, safe: Safe2, input_provider: InputProvider):
        self.safe = safe
        self.input_provider = input_provider
        self.landings = []
    
    def run(self) -> int:
        """Runs the sequence of operations and returns the number of times we landed on or crossed 0."""
        zero_count = 0
        for instruction in self.input_provider.all_instructions():
            crossings = self.safe.apply_instruction(instruction)
            print(f'Applied {instruction} to point at {self.safe.number} with {crossings} crossings')
            zero_count += crossings
            self.landings.append(self.safe.number) # For unit tests

        print(f'Final number {self.safe.number}. Crossed zero {zero_count} times.')
        return zero_count