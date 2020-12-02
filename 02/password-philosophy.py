import re


def passwords(fname):
    pattern = re.compile(r'(?P<min>\d+)-(?P<max>\d+) (?P<letter>[a-z]): (?P<password>[a-z]+)')
    with open('input', 'r') as passwords:
        for line in passwords:
            min, max, letter, password = pattern.match(line).groups()
            yield int(min), int(max), letter, password


if __name__ == '__main__':
    num_valid = 0
    for min, max, letter, password in passwords('input'):
        num = password.count(letter)
        if min <= num <= max:
            num_valid += 1

    print('number of valid passwords:', num_valid)
