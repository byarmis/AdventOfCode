tst = [
    '..@@.@@@@.',
    '@@@.@.@.@@',
    '@@@@@.@.@@',
    '@.@@@@..@.',
    '@@.@@@@.@@',
    '.@@@@@@@.@',
    '.@.@.@.@@@',
    '@.@@@.@@@@',
    '.@@@@@@@@.',
    '@.@.@@@.@.',
]

def part_1(lines):
    cnt = 0
    for line_loc, line in enumerate(lines):
        for loc, val in enumerate(line):
            if val != '@':
                continue
            # Get neighbors
            if line_loc > 0:
                prev_line = lines[line_loc - 1][max(0, loc-1):min(len(line), loc+2)]
            else:
                prev_line = ''

            if line_loc < len(lines) - 1:
                next_line = lines[line_loc + 1][max(0, loc-1):min(len(line), loc+2)]
            else:
                next_line = ''

            current_line = ''
            if loc > 0:
                current_line += line[loc-1]
            if loc < len(line) - 1:
                current_line += line[loc+1]

            if ''.join(prev_line+next_line+current_line).count('@') < 4:
                yield line_loc, loc

assert len(list(part_1(tst))) == 13

with open('input.txt') as f:
    lines = f.readlines()

print('Part 1: ', len(list(part_1(lines))))

def part_2(lines):
    removed = 0
    while any(part_1(lines)):
        new_lines = [list(line) for line in lines]
        for pair in part_1(lines):
            new_lines[pair[0]][pair[1]] = '.'
            removed += 1
        lines = [''.join(line) for line in new_lines]
    return removed

assert part_2(tst) == 43

print('Part 2: ', part_2(lines))

