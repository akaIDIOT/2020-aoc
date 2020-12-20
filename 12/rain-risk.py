def move_ship(instructions):
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

    return coords


def move_with_waypoint(instructions):
    waypoint = [10, 1]
    ship = [0, 0]

    for instruction, amount in instructions:
        if instruction == 'N':
            waypoint[1] += amount
        if instruction == 'S':
            waypoint[1] -= amount
        if instruction == 'E':
            waypoint[0] += amount
        if instruction == 'W':
            waypoint[0] -= amount
        if instruction == 'L':
            if amount == 90:
                waypoint = [-waypoint[1], waypoint[0]]
            if amount == 180:
                waypoint = [-waypoint[0], -waypoint[1]]
            if amount == 270:
                waypoint = [waypoint[1], -waypoint[0]]
        if instruction == 'R':
            if amount == 90:
                waypoint = [waypoint[1], -waypoint[0]]
            if amount == 180:
                waypoint = [-waypoint[0], -waypoint[1]]
            if amount == 270:
                waypoint = [-waypoint[1], waypoint[0]]
        if instruction == 'F':
            ship[0] += amount * waypoint[0]
            ship[1] += amount * waypoint[1]

    return ship


if __name__ == '__main__':
    with open('input', 'r') as instructions:
        instructions = instructions.readlines()
        instructions = [(instruction[0], int(instruction[1:])) for instruction in instructions]

    ship = move_ship(instructions)
    print(f'Location {ship} is {abs(ship[0]) + abs(ship[1])} nautical manhattans from the starting point')

    ship = move_with_waypoint(instructions)
    print(f'Using the waypoint, the ship at {ship} is {abs(ship[0]) + abs(ship[1])} nautical manhattans from the starting point')
