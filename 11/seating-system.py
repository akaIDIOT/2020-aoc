from itertools import product


def parse_input(content):
    translations = {
        '.': 0,
        'L': False,
        '#': True,
    }
    return [[translations[seat] for seat in line.strip()] for line in content.splitlines()]


def select_adjacent(seats, x, y):
    if y > 0:
        # row above
        yield from seats[y - 1][max(x - 1, 0):min(x + 1, len(seats[0])) + 1]

    if x > 0:
        # seat on the left
        yield seats[y][x - 1]
    if x < len(seats[0]) - 1:
        # seat on the right
        yield seats[y][x + 1]

    if y < len(seats[0]) - 1:
        # row below
        yield from seats[y + 1][max(x - 1, 0):min(x + 1, len(seats[0])) + 1]


def state(seats, x, y):
    current_state = seats[y][x]
    if current_state is not False and seats[y][x] == 0:
        # an empty spot stays an empty spot
        return 0

    num_adjacent_occupied = sum(select_adjacent(seats, x, y))
    if not current_state and num_adjacent_occupied == 0:
        # currently empty, no occupied seats surrounding it
        return True
    if current_state and num_adjacent_occupied >= 4:
        # currently occupied, too busy
        return False

    return current_state


def num_occupied(seats):
    return sum(map(sum, seats))


def render(seats):
    def translate(seat):
        if seat is False:
            return 'L'
        if seat is True:
            return '#'
        if seat == 0:
            return '.'

    for row in seats:
        print(''.join(translate(seat) for seat in row))


def apply_rules(seats):
    new_seats = [[state(seats, x, y) for x in range(len(seats[0]))] for y in range(len(seats))]
    num_changed = sum(seats[y][x] is not new_seats[y][x]
                      for y, x in product(range(len(seats)), range(len(seats[0]))))

    return new_seats, num_changed


if __name__ == '__main__':
    with open('input', 'r') as seats:
        seats = parse_input(seats.read())

    num_changed = True
    iterations = 0
    while num_changed:
        seats, num_changed = apply_rules(seats)
        iterations += 1

    print(f'The dust settles after {iterations} iterations, {num_occupied(seats)} seats are occupied')
