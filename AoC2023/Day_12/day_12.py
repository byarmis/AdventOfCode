from collections import deque

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

def springs_to_groupings(springs):
    g = 0
    gs = []

    for val in springs:
        if val == '#':
            g += 1
        elif g > 0:
            gs.append(g)
            g = 0
    if g > 0:
        gs.append(g)

    return gs

def get_arrangements(line):
    springs, groupings = line.split()
    groupings = [int(i) for i in groupings.split(',')]
    springs = list(springs)

    if '?' not in springs:
        return 1

    changed = True
    to_generate = deque()
    to_generate.appendleft(springs)

    generated = set()

    while to_generate:
        new_spring = to_generate.popleft()
        if '?' not in new_spring:
            generated.add(tuple(new_spring))
            continue

        for loc, val in enumerate(new_spring):
            if val == '?':
                a = new_spring.copy()
                b = new_spring.copy()
                a[loc] = '#'
                to_generate.append(a)

                b[loc] = '.'
                to_generate.append(b)

    print(f'generated - {len(generated)}')
    filtered = len([s for s in generated if springs_to_groupings(s) == groupings])
    print(f'filtered - {filtered}')
    return filtered



def part_1(lines):
    return sum(get_arrangements(line) for line in lines)


test_lines = [
        '???.### 1,1,3',
        '.??..??...?##. 1,1,3',
        '?#?#?#?#?#?#?#? 1,3,1,6',
        '????.#...#... 4,1,1',
        '????.######..#####. 1,6,5',
        '?###???????? 3,2,1',
        ]

assert springs_to_groupings('#.#.###') == [1,1,3]
assert springs_to_groupings('.#...#....###.') == [1,1,3]
assert springs_to_groupings('.#.###.#.######') == [1,3,1,6]
assert springs_to_groupings('####.#...#...') == [4,1,1]
assert springs_to_groupings('#....######..#####.') == [1,6,5]
assert springs_to_groupings('.###.##....#') == [3,2,1]

t = part_1(test_lines)
assert t == 21, t

