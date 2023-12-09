
with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]


def get_next(line):
    line = [int(l) for l in line.split()]
    diff_arr = [line]
    diffs = [second-first for first, second in zip(line, line[1:])]
    diff_arr.append(diffs)
    while not all(d == 0 for d in diffs):
        diffs = [second-first for first, second in zip(diff_arr[-1], diff_arr[-1][1:])]
        diff_arr.append(diffs)

    new_val = 0
    for diff in diff_arr[::-1]:
        new_val = new_val + diff[-1]
    return new_val

def get_prev(line):
    line = [int(l) for l in line.split()]
    diff_arr = [line]
    diffs = [second-first for first, second in zip(line, line[1:])]
    diff_arr.append(diffs)
    while not all(d == 0 for d in diffs):
        diffs = [second-first for first, second in zip(diff_arr[-1], diff_arr[-1][1:])]
        diff_arr.append(diffs)

    new_val = 0
    for diff in diff_arr[::-1]:
        new_val = diff[0] - new_val
    return new_val


def part_1(lines):
    return sum(get_next(line) for line in lines)

def part_2(lines):
    return sum(get_prev(line) for line in lines)

test_lines = [
        '0 3 6 9 12 15',
        '1 3 6 10 15 21',
        '10 13 16 21 30 45',
        ]

t = part_1(test_lines)
assert t == 114, t
print('Part 1: ', part_1(lines))

t = part_2(test_lines)
assert t == 2, t
print('Part 2: ', part_2(lines))

