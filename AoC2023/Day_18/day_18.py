with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]


def shoelace(grid):
    grid = list(grid)
    area = 0

    for first, second in zip(grid, grid[1:]):
        x1, y1 = first
        x2, y2 = second
        area += (y1 + y2) * (x1 - x2)
    x1, y1 = grid[-1]
    x2, y2 = grid[0]
    area += (y1 + y2) * (x1 - x2)

    return abs(area)


def part_1(lines):
    grid = set()

    pnt = [0, 0]
    grid.add(tuple(pnt))

    perimeter = 0

    for line in lines:
        d, num, _ = line.split()
        num = int(num)

        dx = 0
        dy = 0
        if d == "U":
            dy = -1
        elif d == "D":
            dy = 1
        elif d == "L":
            dx = -1
        elif d == "R":
            dx = 1
        else:
            raise Exception("Unknown direction")

        pnt[0] += dx * num
        pnt[1] += dy * num
        grid.add(tuple(pnt))
        perimeter += num

    return (shoelace(grid) + perimeter) // 2 + 1


test_lines = [
    "R 6 (#70c710)",
    "D 5 (#0dc571)",
    "L 2 (#5713f0)",
    "D 2 (#d2c081)",
    "R 2 (#59c680)",
    "D 2 (#411b91)",
    "L 5 (#8ceee2)",
    "U 2 (#caa173)",
    "L 1 (#1b58a2)",
    "U 2 (#caa171)",
    "R 2 (#7807d2)",
    "U 3 (#a77fa3)",
    "L 2 (#015232)",
    "U 2 (#7a21e3)",
]


t = part_1(test_lines)
assert t == 62, t

p1 = part_1(lines)

print("Part 1: ", p1)


def part_2(lines):
    grid = set()

    pnt = [0, 0]
    grid.add(tuple(pnt))

    perimeter = 0

    for line in lines:
        _, __, code = line.split()
        num = int(code[2:-2], 16)
        d = code[-2]

        dx = 0
        dy = 0
        if d == "3":
            dy = -1
        elif d == "1":
            dy = 1
        elif d == "2":
            dx = -1
        elif d == "0":
            dx = 1
        else:
            raise Exception("Unknown direction")

        pnt[0] += dx * num
        pnt[1] += dy * num
        grid.add(tuple(pnt))
        perimeter += num

    return (shoelace(grid) + perimeter) // 2 + 1


t = part_2(test_lines)
assert t == 952408144115, t
print("Part 2: ", part_2(lines))
