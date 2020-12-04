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


if __name__ == '__main__':
    required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

    num_valid = 0
    for record in parse_input('input'):
        if set(record.keys()) & required == required:
            num_valid += 1

    print(f'Number of valid passports: {num_valid}')
