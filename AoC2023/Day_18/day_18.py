
with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]


def part_1(lines):
    grid = set()

    pnt = [0,0]
    grid.add(tuple(pnt))

    for line in lines:
        d, num, _ = line.split()
        num = int(num)

        dx = 0
        dy = 0
        if d == 'U':
            dy = 1
        elif d == 'D':
            dy = -1
        elif d == 'L':
            dx = -1
        elif d == 'R':
            dx = 1
        else:
            raise Exception('Unknown direction')

        for _ in range(num):
            pnt[0] += dx
            pnt[1] += dy
            grid.add(tuple(pnt))

    vol = 0

    y_min = min(p[1] for p in grid)
    y_max = max(p[1] for p in grid)

    for row in range(y_min, y_max+1):
        x_min = min(p[0] for p in grid if p[1] == row)
        x_max = max(p[0] for p in grid if p[1] == row)

        to_add = x_max - x_min + 1
        vol += to_add

    return vol


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

p1 = part_1(lines)
assert p1 != 87847

print('Part 1: ', p1)

