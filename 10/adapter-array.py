from collections import Counter


def connect(adapters):
    current = 0
    for adapter in adapters:
        yield adapter - current
        current = adapter

    yield 3  # our own device


if __name__ == '__main__':
    with open('input', 'r') as adapters:
        adapters = [int(line) for line in adapters]
        adapters.sort()

    diffs = Counter(connect(adapters))

    print(f'All adapters together have {diffs[1]} 1-jolt and {diffs[3]} 3-jolt differences ({diffs[1] * diffs[3]})')
