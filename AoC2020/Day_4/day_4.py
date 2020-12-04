import string
import re

with open('input.txt') as f:
    raw = f.readlines()

with open('tst.txt') as f:
    test_raw = f.readlines()


def passports(raw):
    joined = ''
    for p in raw:
        if not p.strip():
            yield joined
            joined = ''
        else:
            joined += ' ' + p.strip()

    yield joined

assert len(list(passports(test_raw))) == 4, list(passports(test_raw))


def part_1(raw):
    required_fields = {
        'byr'
        , 'iyr'
        , 'eyr'
        , 'hgt'
        , 'hcl'
        , 'ecl'
        , 'pid'
    }

    valid_cnt = 0
    for pp in passports(raw):
        valid = True

        for field in required_fields:
            if field in pp:
                valid &= True
            else:
                valid = False
        valid_cnt += int(valid)
    return valid_cnt


assert part_1(test_raw) == 2, part_1(test_raw) 

print('part one: ', part_1(raw))

def part_2(raw):
    def hgt(f):
        if f.endswith('cm'):
            h = f[:-2]
            return 150 <= int(h) <= 193

        elif f.endswith('in'):
            h = f[:-2]
            return 59 <= int(h) <= 76

        else:
            return False

    def hcl(f):
        if f[0] != '#':
            return False
        if len(f) != 7:
            return False
        return not set(f[1:]) - set(string.hexdigits)


    required_fields = {
            'byr': lambda f: 1920 <= int(f) <= 2002,
            'iyr': lambda f: 2010 <= int(f) <= int(2020),
            'eyr': lambda f: 2020 <= int(f) <= int(2030),
            'hgt': hgt,
            'hcl': hcl,
            'ecl': lambda f: f in {'amb' , 'blu' , 'brn' , 'gry' , 'grn' , 'hzl' , 'oth'},
            'pid': lambda f: len(f) == 9,
            }

    valid_cnt = 0
    for pp in passports(raw):
        valid = True
        for field, func in required_fields.items():
            if field not in pp:
                valid = False

            r = re.search(rf'{field}:(.*?)(\s|$)', pp)

            if r:
                valid &= func(r.group(1).strip())
            else:
                valid = False

        valid_cnt += int(valid)

    return valid_cnt

print('part two: ', part_2(raw))

