if __name__ == '__main__':
    with open('input', 'r') as instructions:
        instructions = instructions.readlines()
        instructions = [(instruction[0], int(instruction[1:])) for instruction in instructions]

    coords = [0, 0]
    heading = 90

    for instruction, amount in instructions:
        if instruction == 'N':
            coords[1] += amount
        if instruction == 'S':
            coords[1] -= amount
        if instruction == 'E':
            coords[0] += amount
        if instruction == 'W':
            coords[0] -= amount
        if instruction == 'L':
            heading = (heading - amount) % 360
        if instruction == 'R':
            heading = (heading + amount) % 360
        if instruction == 'F':
            if heading == 0:
                coords[1] += amount
            elif heading == 90:
                coords[0] += amount
            elif heading == 180:
                coords[1] -= amount
            elif heading == 270:
                coords[0] -= amount
            else:
                raise ValueError(f'invalid current heading: {heading}')

    print(f'Location {coords} is {abs(coords[0]) + abs(coords[1])} nautical units from the starting point')
