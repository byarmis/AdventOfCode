
with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

def shoelace(grid):
    grid = list(grid)
    area = 0

    for i, j in zip(grid, grid[1:]):
        area += (i[1]+j[1]) * (i[0] - j[0])
    i = grid[-1]
    j = grid[0]
    area += (i[1]+j[1]) * (i[0] - j[0])
    print('a',area)

    return abs(area)

def part_1(lines):
    grid = set()

    pnt = [0,0]
    grid.add(tuple(pnt))

    perimeter = 0

    for line in lines:
        d, num, _ = line.split()
        num = int(num)

        dx = 0
        dy = 0
        if d == 'U':
            dy = -1
        elif d == 'D':
            dy = 1
        elif d == 'L':
            dx = -1
        elif d == 'R':
            dx = 1
        else:
            raise Exception('Unknown direction')

        pnt[0] += dx * num
        pnt[1] += dy * num
        grid.add(tuple(pnt))
        perimeter += num

    print('p',perimeter)
    return shoelace(grid) + perimeter

test_lines = [
    'R 6 (#70c710)',
    'D 5 (#0dc571)',
    'L 2 (#5713f0)',
    'D 2 (#d2c081)',
    'R 2 (#59c680)',
    'D 2 (#411b91)',
    'L 5 (#8ceee2)',
    'U 2 (#caa173)',
    'L 1 (#1b58a2)',
    'U 2 (#caa171)',
    'R 2 (#7807d2)',
    'U 3 (#a77fa3)',
    'L 2 (#015232)',
    'U 2 (#7a21e3)',
]


t = part_1(test_lines)
assert t == 62, t

chrstine_test = [
    'R 3 x', 
    'D 3 x', 
    'R 3 x', 
    'U 3 x', 
    'R 3 x', 
    'D 9 x', 
    'L 3 x', 
    'U 3 x', 
    'L 3 x', 
    'D 3 x', 
    'L 3 x', 
    'U 9 x', 
    ]

t = part_1(chrstine_test)

assert t == 88, t

p1 = part_1(lines)
assert p1 != 87847

print('Part 1: ', p1)

