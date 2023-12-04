import itertools
import math
from collections import defaultdict

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

def solve(lines):
    nums = []
    gears = defaultdict(list)
    for y, line in enumerate(lines):
        num = ''
        for x, char in enumerate(line):
            if char.isdigit():
                num += char
            if (char.isdigit() and x == len(line) - 1) or (not char.isdigit() and num):
                dx = {-1, 0}
                dy = {-1, 0, 1}

                if char.isdigit():
                    dx.add(1)

                for num_idx in range(int(char.isdigit()), len(num) + 2 - int(char.isdigit())):
                    dx.add(-num_idx)

                candidates = set()
                for x_mod, y_mod in itertools.product(dx, dy):
                    if x + x_mod < 0 or x+x_mod > len(line) - 1:
                        continue
                    if y + y_mod < 0 or y+y_mod > len(lines) - 1:
                        continue

                    candidate = lines[y+y_mod][x+x_mod]
                    if candidate == '*':
                        gears[(x+x_mod, y+y_mod)].append(int(num))

                    candidates.add(candidate)

                if any(candidates - set('1234567890.')):
                    nums.append(int(num))

                num = ''

    return sum(nums), sum([gear[0] * gear[1] for gear in gears.values() if len(gear) == 2])

provided_lines = [
        '467..114.', 
        '...*.....', 
        '..35..633', 
        '......#..', 
        '617*.....', 
        '.....+.58', 
        '..592....', 
        '......755', 
        '...$.*...', 
        '.664.598.', 
        ]

test_cases = {
        4361 : provided_lines,
        4361 : [line+'.' for line in provided_lines],
        4361 : ['.'+line for line in provided_lines],
        4361 : ['.'+line+'.' for line in provided_lines],
        123+45+6 : [
            '.123...',
            '45++6..',
            ],
        123: [
            '..+..',
            '.123.',
            ],
        0 : [
            '....+.',
            '123...',
            ],
        }

for expected, test_lines in test_cases.items():
    test = solve(test_lines)[0]
    assert  test == expected, f'{expected} expected, got {test}'

solution = solve(lines)[0]
assert solution != 554613, solution 
assert solution != 552006, solution 
assert solution != 552463, solution 
assert solution != 536628, solution 
assert solution != 536171, solution 

print('Part 1: ', solve(lines)[0])
print('Part 2: ', solve(lines)[1])

