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
        passes = sorted(to_seat_id(boarding_pass.strip()) for boarding_pass in passes)

    highest = max(passes)

    missing = None
    for idx in range(len(passes) - 1):
        if passes[idx] + 2 == passes[idx + 1]:
            missing = passes[idx] + 1

    print(f'Highest seat ID: {highest}')
    print(f'Missing seat ID: {missing}')
