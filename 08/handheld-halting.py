class LoopError(ValueError):
    def __init__(self, accumulator):
        self.accumulator = accumulator


def run(program):
    accumulator = 0
    program_counter = 0

    visited = set()

    while program_counter < len(program):
        if program_counter in visited:
            raise LoopError(accumulator)

        instruction, operand = program[program_counter]
        visited.add(program_counter)

        if instruction == 'nop':
            program_counter += 1
        elif instruction == 'acc':
            accumulator += operand
            program_counter += 1
        elif instruction == 'jmp':
            program_counter += operand
        else:
            raise ValueError(f'illegal instruction: {instruction}')

    return accumulator


def patch(program):
    for idx, (instruction, operand) in enumerate(program):
        if instruction == 'nop':
            yield program[:idx] + [('jmp', operand)] + program[idx + 1:]
        elif instruction == 'jmp':
            yield program[:idx] + [('nop', operand)] + program[idx + 1:]


if __name__ == '__main__':
    with open('input', 'r') as program:
        program = [line.split() for line in program.readlines()]
        program = [(instruction, int(operand)) for instruction, operand in program]

    try:
        run(program)
    except LoopError as e:
        print(f'Accumulator at first repeated instruction: {e.accumulator}')

    for patched in patch(program):
        try:
            accumulator = run(patched)
        except LoopError:
            pass  # that wasn't it…
        else:
            print(f'Accumulator using patched program: {accumulator}')
