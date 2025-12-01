from day1 import InputProvider, FileInputProvider


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

        new_number = self.number + sign * units
        if new_number < 0 or new_number >= self.spots:
            extra_crossings = abs(new_number) // self.spots
            # When the new number is negative, we definitely crossed once
            # even if abs(new_number) is less than the number of spots.
            # So if new number is 12 we crossed zero times. But if it's -12 we crossed once.
            # Don't count extra crossing if we started at zero, because that's already been counted previously.
            if new_number < 0 and self.number != 0:
                extra_crossings += 1 # -1 means 1 crossing. -101 means 2 crossings.
        else:
            extra_crossings = 0
        #print(f'{new_number=} {extra_crossings=}')
        self.number = new_number % self.spots
        
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
            origin = self.safe.number
            crossings = self.safe.apply_instruction(instruction)
            print(f'Applied {instruction} from {origin} to {self.safe.number} with {crossings} crossings')
            zero_count += crossings
            self.landings.append(self.safe.number) # For unit tests

        print(f'Final number {self.safe.number}. Crossed zero {zero_count} times.')
        return zero_count

def main():
    input_provider = FileInputProvider('day1_input.txt')
    safe = Safe2()
    operator = SafeOperator2(safe, input_provider)
    zero_count = operator.run()
    print(f'Answer: {zero_count}')

if __name__ == '__main__':
    main()