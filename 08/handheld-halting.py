def run_to_loop(program):
    accumulator = 0
    program_counter = 0

    visited = set()

    while program_counter not in visited:
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


if __name__ == '__main__':
    with open('input', 'r') as program:
        program = [line.split() for line in program.readlines()]
        program = [(instruction, int(operand)) for instruction, operand in program]

    accumulator = run_to_loop(program)

    print(f'Accumulator at first repeated instruction: {accumulator}')
