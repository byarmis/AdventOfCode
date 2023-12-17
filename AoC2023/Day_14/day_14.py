from functools import cache
from typing import Tuple, List, AbstractSet, Literal

CubeSet = AbstractSet[Tuple[int, int]]
Delta = Literal[-1, 0, 1]


def torque(num_lines:int, rocks:CubeSet) -> int:
    return sum(num_lines - rock[0] for rock in rocks)


@cache
def roll(round_rocks:CubeSet, cubes:CubeSet, dy:Delta, dx:Delta, max_y:int, max_x:int) -> CubeSet:
    changed = True

    while changed:
        changed = False
        new_round_rocks = set()

        for rock in round_rocks:
            if rock[0] == 0 and dy < 0:
                new_round_rocks.add(rock)
            elif rock[0] == max_y-1 and dy > 0:
                new_round_rocks.add(rock)

            elif rock[1] == 0 and dx < 0:
                new_round_rocks.add(rock)
            elif rock[1] == max_x-1 and dx > 0:
                new_round_rocks.add(rock)

            elif (rock[0]+dy, rock[1]+dx) in cubes or (rock[0]+dy, rock[1]+dx) in round_rocks:
                # There's something in the way.  The other round rock might move later though
                new_round_rocks.add(rock)

            else:
                # Move the rock
                new_round_rocks.add((rock[0]+dy, rock[1]+dx))
                changed = True

        round_rocks = new_round_rocks

    return frozenset(round_rocks)


def get_rocks_and_cubes(lines:List[str]) -> Tuple[CubeSet, CubeSet]:
    round_rocks = set()
    cubes = set()

    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            if c == 'O':
                round_rocks.add((y, x))
            elif c == '#':
                cubes.add((y,x))

    return frozenset(round_rocks), frozenset(cubes)


def part_1(lines:List[str]) -> int:
    round_rocks, cubes = get_rocks_and_cubes(lines)
    round_rocks = roll(round_rocks, cubes, -1, 0, len(lines), len(lines[0]))
    return torque(len(lines), round_rocks)


def part_2(lines:List[str]) -> int:
    cycles = 1_000_000_000

    round_rocks, cubes = get_rocks_and_cubes(lines)

    max_y = len(lines)
    max_x = len(lines[0])

    roll.cache_clear()
    prev_cache_size = None

    for i in range(cycles):
        round_rocks = roll(round_rocks, cubes, -1, 0, max_y, max_x) # North
        round_rocks = roll(round_rocks, cubes, 0, -1, max_y, max_x) # West
        round_rocks = roll(round_rocks, cubes, 1, 0, max_y, max_x) # South
        round_rocks = roll(round_rocks, cubes, 0, 1, max_y, max_x) # East

        if prev_cache_size is None:
            prev_cache_size = roll.cache_info().currsize
        elif prev_cache_size == roll.cache_info().currsize:
            break
        else:
            prev_cache_size = roll.cache_info().currsize

    return torque(len(lines), round_rocks)


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

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

print('Part 1: ', part_1(lines))

t = part_2(test_lines)
assert t == 64, t

print('Part 2: ', part_2(lines))

