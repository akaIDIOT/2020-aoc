to_binary = str.maketrans({
    'B': '1',
    'F': '0',
    'R': '1',
    'L': '0',
})


def to_seat_id(boarding_pass):
    boarding_pass = boarding_pass.translate(to_binary)
    return int(boarding_pass[:7], 2) * 8 + int(boarding_pass[7:], 2)


if __name__ == '__main__':
    with open('input', 'r') as passes:
        highest = max(to_seat_id(boarding_pass.strip()) for boarding_pass in passes)

    print(f'Highest seat ID: {highest}')
