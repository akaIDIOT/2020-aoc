def get_adjacent(seats, x, y, width, height):
    adjacent = []

    if y > 0:
        # row above (x, y)
        adjacent.append(seats[y - 1][max(0, x - 1):min(x + 1, width) + 1])

    if x > 0:
        # seat to the left
        adjacent.append(seats[y][x - 1])
    if x < width - 1:
        # seat to the right
        adjacent.append(seats[y][x + 1])

    if y < height - 1:
        # row below (x, y)
        adjacent.append(seats[y + 1][max(0, x - 1):min(x + 1, width) + 1])

    return ''.join(adjacent)


def seat_in_direction(seats, x, y, width, height, dx, dy):
    seat = '.'

    # set a step
    x += dx
    y += dy

    while seat == '.' and 0 <= x < width and 0 <= y < height:
        # visible seat after step
        seat = seats[y][x]
        # set a step
        x += dx
        y += dy

    return seat


def get_visible(seats, x, y, width, height):
    visible = []
    directions = (
        (-1, -1),  # north-west
        ( 0, -1),  # north
        ( 1, -1),  # north-east
        (-1,  0),  # west
        ( 1,  0),  # east
        (-1,  1),  # south-west
        ( 0,  1),  # south
        ( 1,  1),  # south-east
    )

    for dx, dy in directions:
        if seat := seat_in_direction(seats, x, y, width, height, dx, dy):
            visible.append(seat)

    return ''.join(visible)


def determine_seat(seats, x, y, width, height, mode, tolerance):
    if seats[y][x] == '.':
        # empty places remain empty
        return '.'

    if mode == 'adjacency':
        applicable = get_adjacent(seats, x, y, width, height)
    elif mode == 'visibility':
        applicable = get_visible(seats, x, y, width, height)
    else:
        raise ValueError(f'invalid mode: {mode}')

    if seats[y][x] == 'L' and applicable.count('#') == 0:
        # empty surrounded by empty -> occupied
        return '#'
    if seats[y][x] == '#' and applicable.count('#') >= tolerance:
        # occupied surrounded by tolerance or more occupied -> empty
        return 'L'

    # no change
    return seats[y][x]


def step(seats, mode, tolerance):
    width = len(seats[0])
    height = len(seats)

    new_seats = []
    num_changed = 0
    for y, row in enumerate(seats):
        new_row = []
        for x, seat in enumerate(row):
            new_seat = determine_seat(seats, x, y, width, height, mode=mode, tolerance=tolerance)
            num_changed += seat != new_seat
            new_row.append(new_seat)

        new_seats.append(''.join(new_row))

    return new_seats, num_changed


def num_occupied(seats):
    return sum(row.count('#') for row in seats)


if __name__ == '__main__':
    with open('input', 'r') as seats:
        seats = [line.strip() for line in seats.readlines()]

    iterations = 0
    num_changed = 1
    while num_changed > 0:
        seats, num_changed = step(seats, mode='adjacency', tolerance=4)
        iterations += 1

    print(f'The dust settles after {iterations} iterations, {num_occupied(seats)} seats are occupied')

    with open('input', 'r') as seats:
        seats = [line.strip() for line in seats.readlines()]

    iterations = 0
    num_changed = 1
    while num_changed > 0:
        seats, num_changed = step(seats, mode='visibility', tolerance=5)
        iterations += 1

    print(f'The dust settles again after {iterations} iterations, {num_occupied(seats)} seats are now occupied')
