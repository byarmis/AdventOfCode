
with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

def part_1(lines):
    round_rocks = set()
    cubes = set()

    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            if c == 'O':
                round_rocks.add((y, x))
            elif c == '#':
                cubes.add((y,x))

    changed = True
    while changed:
        changed = False
        new_round_rocks = set()

        for rock in round_rocks:
            if rock[0] == 0:
                new_round_rocks.add((rock[0], rock[1]))
            elif (rock[0]-1, rock[1]) in cubes or (rock[0]-1, rock[1]) in round_rocks:
                new_round_rocks.add((rock[0], rock[1]))
            else:
                new_round_rocks.add((rock[0]-1, rock[1]))
                changed = True

        round_rocks = new_round_rocks

    torque = 0
    for rock in round_rocks:
        torque += len(lines) - rock[0]

    return torque

test_lines = [
        'O....#....',
        'O.OO#....#',
        '.....##...',
        'OO.#O....O',
        '.O.....O#.',
        'O.#..O.#.#',
        '..O..#O..O',
        '.......O..',
        '#....###..',
        '#OO..#....',
        ]

t = part_1(test_lines)
assert t == 136, t

print('Part 1: ', part_1(lines))

