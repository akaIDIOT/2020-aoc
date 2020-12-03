if __name__ == '__main__':
    trees = 0
    x = 0

    with open('input', 'r') as geology:
        next(geology)  # skip line 1
        for line in geology:
            line = line.strip()
            x = (x + 3) % len(line)
            if line[x] == '#':
                trees += 1

    print(trees)
