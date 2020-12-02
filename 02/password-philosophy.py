import re


def passwords(fname):
    pattern = re.compile(r'(?P<min>\d+)-(?P<max>\d+) (?P<letter>[a-z]): (?P<password>[a-z]+)')
    with open(fname, 'r') as passwords:
        for line in passwords:
            pos1, pos2, letter, password = pattern.match(line).groups()
            yield int(pos1), int(pos2), letter, password


if __name__ == '__main__':
    num_valid_rental = 0
    num_valid_toboggan = 0

    for pos1, pos2, letter, password in passwords('input'):
        num = password.count(letter)
        if pos1 <= num <= pos2:
            num_valid_rental += 1

        if (password[pos1 - 1] == letter) ^ (password[pos2 - 1] == letter):
            num_valid_toboggan += 1

    print('number of valid sled rental passwords:', num_valid_rental)
    print('number of valid toboggan passwords:', num_valid_toboggan)
