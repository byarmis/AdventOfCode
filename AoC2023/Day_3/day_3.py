import itertools

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

def solve(lines):
    nums = []
    for y, line in enumerate(lines):
        num = ''
        for x, char in enumerate(line):
            if char.isdigit():
                num += char
            if (char.isdigit() and x == len(line) - 1) or (not char.isdigit() and num):
                dx = [-1, 0, 1]
                dy = [-1, 0, 1]

                for num_idx in range(1, len(num) + 2 - int(char.isdigit())):
                    dx.append(-num_idx)

                candidates = []
                for x_mod, y_mod in itertools.product(dx, dy):
                    if char.isdigit():
                        x_mod_limit = 0 >= x_mod > -len(num)
                    else:
                        x_mod_limit = 0 > x_mod >= -len(num) 

                    if x_mod_limit and y_mod == 0:
                        continue
                    if x + x_mod < 0 or x+x_mod > len(line) - 1:
                        continue
                    if y + y_mod < 0 or y+y_mod > len(lines) - 1:
                        continue

                    candidates.append(lines[y+y_mod][x+x_mod])
                if any(x != '.' and not x.isdigit() for x in candidates):
                    nums.append(int(num))

                num = ''
    return sum(nums)

test_lines_1 = [
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
        '.+12....1', 
        '11.....+1', 
        '1......1+', 
        ]
test_lines_2 = [line+'.' for line in test_lines_1]
test_lines_3 = ['.'+line for line in test_lines_1]
test_lines_4 = ['.'+line+'.' for line in test_lines_1]

test_lines_5 = [
        '..4361....',
        '.24+++2...',
        ]


test_lines = [
        test_lines_1,
        test_lines_2,
        test_lines_3,
        test_lines_4,
        test_lines_5,
        ]

for loc, test_line in enumerate(test_lines):
    test = solve(test_line)
    assert  test == 4361+26, f'{loc}: {4361+14} expected, got {test}'

print('tests pass')

assert solve(lines) != 554613
assert solve(lines) != 552006
assert solve(lines) != 552463
assert solve(lines) != 536628
assert solve(lines) != 536171
print('Part 1: ', solve(lines))

