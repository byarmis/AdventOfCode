
from collections import defaultdict
from functools import lru_cache

def serialize(woods, size):
    rows= []
    for row in range(size):
        rows.append(''.join(woods[row, i] for i in range(size)))

    return ''.join(rows)

def get_count(woods):
    wood_count = 0
    lumber_count = 0
    for cell in woods.values():
        if cell == '|':
            wood_count += 1
        elif cell == '#':
            lumber_count += 1

    return wood_count, lumber_count


def get_adjacent_cells(woods, coords):
    row, col = coords

    above = [woods[(row-1, col-1)],
             woods[(row-1, col)],
             woods[(row-1, col+1)]]

    same_row = [woods[row, col-1], 
                woods[row, col+1]]

    below = [woods[row+1, col-1],
             woods[row+1, col],
             woods[row+1, col+1]]

    return [w for w in above+same_row+below if w is not None]

def get_next(woods, size):
    new_woods = defaultdict(lambda: None)
    for row in range(size):
        for col in range(size):
            coord = (row, col)
            current_val = woods[coord]

            if current_val == '.':
                if get_adjacent_cells(woods, (coord)).count('|') >= 3:
                    new_val = '|'
                else:
                    new_val = current_val

            if current_val == '|':
                if get_adjacent_cells(woods, (coord)).count('#') >= 3:
                    new_val = '#'
                else:
                    new_val = current_val

            if current_val == '#':
                if get_adjacent_cells(woods, (coord)).count('#') >= 1 and \
                    get_adjacent_cells(woods, (coord)).count('|') >= 1:
                    new_val = '#'
                else:
                    new_val = '.'

            new_woods[(row, col)] = new_val

    return new_woods

def solve(raw_woods, num_min=10):
    woods = defaultdict(lambda: None)

    for row_loc, row_val in enumerate(raw_woods):
        for col_loc, col_val in enumerate(row_val):
            woods[(row_loc, col_loc)] = col_val.strip()

    i = 0
    found_period = False
    seen = {}

    while i < num_min:
        woods = get_next(woods, size=len(raw_woods))
        i += 1

        if not found_period:
            k = serialize(woods, len(raw_woods))

        if not found_period and k in seen:
            period = i - seen[k]

            while i < num_min - period:
                i += period

            found_period = True

        if not found_period:
            seen[k] = i

    wood_count, lumber_count = get_count(woods)
    return wood_count * lumber_count

with open('input.txt') as f:
    woods = f.readlines()

test_input = [
        '.#.#...|#.',
        '.....#|##|',
        '.|..|...#.',
        '..|#.....#',
        '#.#|||#|#|',
        '...#.||...',
        '.|....|...',
        '||...#|.#|',
        '|.||||..|.',
        '...#.|..|.',
]

assert solve(test_input) == 1147, solve(test_input)

print('Part 1', solve(woods))
print('Part 2', solve(woods, 1000000000))
