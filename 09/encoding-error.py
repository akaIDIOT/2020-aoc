preamble_length = 25


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
