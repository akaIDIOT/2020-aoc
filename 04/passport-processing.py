import re


def parse_input(fname):
    with open(fname, 'r') as in_file:
        record = {}
        for line in in_file:
            line = line.strip()
            if not line:
                yield record
                record = {}
            else:
                record.update(entry.split(':') for entry in line.split())

        if record:
            yield record


def validate_height(height):
    if height.endswith('cm'):
        return 150 <= int(height[:-2]) <= 193
    elif height.endswith('in'):
        return 59 <= int(height[:-2]) <= 76
    else:
        return False


if __name__ == '__main__':
    required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    valid = {
        'byr': lambda year: 1920 <= int(year) <= 2002,
        'iyr': lambda year: 2010 <= int(year) <= 2020,
        'eyr': lambda year: 2020 <= int(year) <= 2030,
        'hgt': validate_height,
        'hcl': lambda color: re.match(r'^#[a-f0-9]{6}$', color),
        'ecl': lambda color: color in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
        'pid': lambda number: re.match(r'^[0-9]{9}$', number),
    }

    num_valid = 0
    num_really_valid = 0
    for record in parse_input('input'):
        if set(record.keys()) & required == required:
            num_valid += 1
            if all(is_valid(record.get(key)) for key, is_valid in valid.items()):
                num_really_valid += 1

    print(f'Number of valid passports: {num_valid}')
    print(f'Number of really valid passports: {num_really_valid}')
