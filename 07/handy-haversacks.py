from collections import defaultdict
import re


def parse_rule(line):
    outer, inners = line.split(' bags contain ')
    inners = re.split(r' bags?[,\.]\s*', inners)
    inners = [inner.split(maxsplit=1) for inner in inners if inner and inner != 'no other']
    inners = {color: int(num) for num, color in inners}

    return outer, inners


if __name__ == '__main__':
    requirements = defaultdict(set)

    with open('input', 'r') as in_file:
        for line in in_file:
            inner, outers = parse_rule(line.strip())
            for outer, _ in outers.items():
                requirements[outer].add(inner)

    start = 'shiny gold'
    known = set(requirements[start])
    seen = set()
    while fringe := known - seen:
        for bag in fringe:
            known.update(requirements[bag])
            seen.add(bag)

    print(f'Number of bags that contain at least one {start} bag: {len(known)}')
