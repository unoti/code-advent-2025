from day1 import InputProvider, FileInputProvider


class Safe2:
    def __init__(self, starting_number: int = 50):
        self.number = 50
        self.spots = 100

    def apply_instruction(self, instruction: str) -> int:
        """Apply an instruction and return how many times we crossed zero."""
        direction = instruction[0]
        units = int(instruction[1:])
        if not units:
            raise ValueError(f'Invalid unit {units}')
        if direction not in ['L', 'R']:
            raise ValueError(f'Instruction {instruction} is not valid')

        if direction == 'L':
            sign = -1
        else:
            sign = 1

        # Python's // operator works interestingly with negative numbers.
        # 10 // 3 = 3, but -10 // 3 = -4.  Good times, good times.

        full_rotations = units // self.spots # units are always positive, so we avoid special math on negatives.
        partial_movement = units % self.spots # Remaining movement after full rotations.
        new_number = (self.number + sign * units) % self.spots
        # Partial crossing detection
        if self.number == 0:
            # If we started at zero we don't count a partial crossing because it was counted last round.
            partial_crossing = False
        elif sign > 0:
            # >= because we need to catch landing right on the boundary.
            partial_crossing = self.number + partial_movement >= self.spots 
        else:
            # is it enough to go over the edge? >= to catch landing right on the boundary.
            partial_crossing = partial_movement >= self.number
        zero_crosses = full_rotations
        if partial_crossing:
            zero_crosses += 1

        #print(f'{units=} {new_number=} {sign=} {full_rotations=} {partial_movement=} {partial_crossing=}')
        self.number = new_number
        return zero_crosses


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