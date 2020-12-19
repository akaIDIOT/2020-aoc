from collections import Counter
from itertools import combinations
from math import prod


def connect(adapters):
    current = 0
    for adapter in adapters:
        yield adapter - current
        current = adapter

    yield 3  # our own device


def groups(adapters):
    current = 0
    start = current
    group = []

    for adapter in adapters:
        if adapter - current == 1:
            group.append(adapter)

        if adapter - current == 3:
            yield start, group, adapter
            start = adapter
            group = []

        current = adapter

    yield start, group, adapter + 3


def possible(start, group, end):
    current = start

    for adapter in group:
        if adapter - current > 3:
            return False
        current = adapter

    if end - current > 3:
        return False

    return True


def arrangements(start, group, end):
    if len(group) < 2:
        return 1

    n = 0
    for amount in range(1, len(group) + 1):
        n += sum(possible(start, intermediate, end) for intermediate in combinations(group, amount))

    return n


if __name__ == '__main__':
    with open('input', 'r') as adapters:
        adapters = [int(line) for line in adapters]
        adapters.sort()

    diffs = Counter(connect(adapters))

    print(f'All adapters together have {diffs[1]} 1-jolt and {diffs[3]} 3-jolt differences '
          f'({diffs[1] * diffs[3]})')

    print(f'Total number of possible arrangements: '
          f'{prod(arrangements(start, group, end) for start, group, end in groups(adapters))}')
