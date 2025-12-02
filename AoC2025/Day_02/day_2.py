import math

def get_problem():
    with open('input.txt') as f:
        return f.readline()

def part_1(i):
    i = str(i)

    for subset_length in range(1, len(i)):
        base_stem = i[:subset_length]
        num = base_stem + base_stem

        if num == i:
            return True
    return False


def solve(s, has_dupe):
    invalid_sum = 0
    for r in s.split(','):
        s, e = r.split('-')
        for i in range(int(s), int(e)+1):
            if has_dupe(i):
                invalid_sum += i
    return invalid_sum

tst = '11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'
assert part_1(11)
assert part_1(1188511885)
assert solve(tst, part_1) == 1227775554
 
print('Part 1: ', solve(get_problem(), part_1))

def part_2(i):
    i = str(i)

    for subset_length in range(1, len(i)):
        base_stem = i[:subset_length]
        num = ''
        while len(num) < len(i):
            num += base_stem
            if num == i:
                return True

    return False

assert solve(tst, part_2) == 4174379265

print('Part 2: ', solve(get_problem(), part_2))

