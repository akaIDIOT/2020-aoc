from itertools import combinations


if __name__ == '__main__':
    with open('input', 'r') as expenses:
        expenses = {int(line) for line in expenses}

    for a, b in combinations(expenses, 2):
        if a + b == 2020:
            print(f'{a} * {b}:', a * b)
