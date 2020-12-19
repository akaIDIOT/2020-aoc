preamble_length = 25


def sum_target(xmas, start, target):
    for idx in range(start, len(xmas)):
        candidate = sum(xmas[start:idx])
        if candidate == target:
            return xmas[start:idx]
        if candidate > target:
            return None


if __name__ == '__main__':
    with open('input', 'r') as xmas:
        xmas = [int(line) for line in xmas]
        pool, xmas = xmas[:preamble_length], xmas[preamble_length:]

    for n in xmas:
        if any(n - a in pool for a in pool):
            pool.pop(0)
            pool.append(n)
        else:
            print(f'Invalid XMAS number: {n}')
            break

    with open('input', 'r') as xmas:
        xmas = [int(line) for line in xmas]

    target_number = n
    for idx in range(len(xmas)):
        if result := sum_target(xmas, idx, n):
            result.sort()
            print(f'Encryption weakness is {result[0]} + {result[-1]}: {result[0] + result[-1]}')
            break
