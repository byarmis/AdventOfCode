
with open('input.txt') as f:
    lines = f.readlines()

def part_1(lines):
    nums = []
    for y, line in enumerate(lines):
        num = ''
        for x, char in enumerate(line):
            if char.isdigit():
                num += char
            if (char.isdigit() and x == len(line) - 1) or (not char.isdigit()) and num:

                # If is adjacent to symbol
                dx = [0]
                dy = [0]

                if x > 0:
                    dx.append(-1)
                if y > 0:
                    dy.append(-1)
                if x < len(line) - 1:
                    dx.append(1)
                if y < len(lines) - 1:
                    dy.append(1)

                for num_idx in range(1, len(num) + 2 - int(char.isdigit())):
                    dx.append(-num_idx)

                candidates = []
                for x_mod in dx:
                    for y_mod in dy:
                        if char.isdigit():
                            x_mod_limit = 0 >= x_mod >= -len(num)
                        else:
                            x_mod_limit = 0 > x_mod >= -len(num)

                        if x_mod_limit and y_mod == 0:
                            continue
                        if x + x_mod < 0 or x+x_mod > len(line):
                            continue
                        if y + y_mod < 0 or y+y_mod > len(lines):
                            continue

                        candidates.append(lines[y+y_mod][x+x_mod])
                if not all(x == '.' for x in candidates) and num: 
                    nums.append(int(num))

                num = ''
    return sum(nums)

test_lines_1 = [
        '.........', 
        '.........', 
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
        '.........', 
        '.........', 
        ]
test_lines_2 = [line+'.' for line in test_lines_1]
test_lines_3 = ['.'+line for line in test_lines_1]
test_lines_4 = ['.'+line+'.' for line in test_lines_1]

test_lines = [test_lines_1, test_lines_2, test_lines_3, test_lines_4]

for loc, test_line in enumerate(test_lines):
    test = part_1(test_line)
    assert  test == 4361, f'{loc}: {test}'

print('Part 1: ', part_1(lines))

