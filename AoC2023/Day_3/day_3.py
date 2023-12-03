
with open('input.txt') as f:
    lines = f.readlines()

def part_1(lines):
    nums = []
    for y, line in enumerate(lines):
        num = ''
        for x, char in enumerate(line):
            if char.isdigit():
                num += char
            elif num:
                # If is adjacent to symbol
                dx = [0]
                dy = [0]

                if x > 1:
                    dx.append(-1)
                if y > 1:
                    dy.append(-1)
                if x < len(line) - 1:
                    dx.append(1)
                if y < len(lines) - 1:
                    dy.append(1)

                for num_idx in range(len(num)+2):
                    dx.append(-num_idx)

                candidates = []
                for x_mod in dx:
                    for y_mod in dy:
                        if 0 > x_mod >= -len(num) and y_mod == 0:
                            continue
                        if x + x_mod < 0 or x+x_mod > len(line):
                            continue

                        if y + y_mod < 0 or y+y_mod > len(lines):
                            continue

                        candidates.append(lines[y+y_mod][x+x_mod])
                
                if not all(x == '.' for x in candidates):
                    nums.append(int(num))
                num = ''
    return sum(nums)

test_lines = [
        '467..114..', 
        '...*......', 
        '..35..633.', 
        '......#...', 
        '617*......', 
        '.....+.58.', 
        '..592.....', 
        '......755.', 
        '...$.*....', 
        '.664.598..', 
        ]
assert part_1(test_lines) == 4361
print('Part 1: ', part_1(lines))

