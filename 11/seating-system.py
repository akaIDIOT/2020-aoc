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


def determine_seat(seats, x, y, width, height):
    if seats[y][x] == '.':
        # empty places remain empty
        return '.'

    adjacent = get_adjacent(seats, x, y, width, height)
    if seats[y][x] == 'L' and adjacent.count('#') == 0:
        # empty surrounded by empty -> occupied
        return '#'
    if seats[y][x] == '#' and adjacent.count('#') >= 4:
        # occupied surrounded by 4 or more occupied -> empty
        return 'L'

    # no change
    return seats[y][x]


def step(seats):
    width = len(seats[0])
    height = len(seats)

    new_seats = []
    num_changed = 0
    for y, row in enumerate(seats):
        new_row = []
        for x, seat in enumerate(row):
            new_seat = determine_seat(seats, x, y, width, height)
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
        seats, num_changed = step(seats)
        iterations += 1

    print(f'The dust settles after {iterations} iterations, {num_occupied(seats)} seats are occupied')
