import string


def groups(fname):
    with open(fname, 'r') as in_file:
        group = set()
        for line in in_file:
            line = line.strip()
            if line:
                group.add(line)
            else:
                yield group
                group = set()

        if group:
            yield group


def acks(group):
    questions = set()
    for person in group:
        questions.update(person)

    return questions


def all_acks(group):
    questions = set(string.ascii_lowercase)

    for person in group:
        questions.intersection_update(set(person))

    return questions


if __name__ == '__main__':
    total = sum(len(acks(group)) for group in groups('input'))
    print(f'Sum of counts: {total}')

    total = sum(len(all_acks(group)) for group in groups('input'))
    print(f'Sum of intersection counts: {total}')
