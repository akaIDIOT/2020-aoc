if __name__ == '__main__':
    with open('input', 'r') as geology:
        geology = [line.strip() for line in geology]

    product = 1
    for dx, dy in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        x = y = trees = 0
        while y < len(geology):
            if geology[y][x] == '#':
                trees += 1
            x = (x + dx) % len(geology[0])
            y += dy

        print(f'Right {dx}, down {dy}: {trees}')
        product *= trees

    print(f'Product: {product}')
