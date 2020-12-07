from collections import defaultdict
import re


def parse_rule(line):
    outer, inners = line.split(' bags contain ')
    inners = re.split(r' bags?[,\.]\s*', inners)
    inners = [inner.split(maxsplit=1) for inner in inners if inner and inner != 'no other']
    inners = {color: int(num) for num, color in inners}

    return outer, inners


def num_bags(forward, color):
    if not forward.get(color):
        return 0

    inners = forward.get(color)
    return sum(inners.values()) + sum((num * num_bags(forward, inner)) for inner, num in inners.items())


if __name__ == '__main__':
    reverse = defaultdict(set)
    forward = {}

    with open('input', 'r') as in_file:
        for line in in_file:
            outer, inners = parse_rule(line.strip())
            forward[outer] = inners
            for inner, num in inners.items():
                reverse[inner].add(outer)

    start = 'shiny gold'
    known = set(reverse[start])
    seen = set()
    while fringe := known - seen:
        for bag in fringe:
            known.update(reverse[bag])
            seen.add(bag)

    print(f'Number of bags that contain at least one {start} bag: {len(known)}')

    print(f'Total number of bags inside the {start} bag: {num_bags(forward, start)}')
