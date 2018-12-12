import re
from itertools import chain
from collections import defaultdict

def get_next_state(s, maps):
    next_state = []
    offset = 0
    if sum(s[-4:]) > 0:
        # The last 4 have a filled pot, append
        s += [False]*4
    if sum(s[:4]) > 0:
        # The first 4 have a filled pot, prepend
        s = [False]*4 + s
        offset = 4

    for i in range(2, len(s)-3):
        k = tuple(s[i-2:i+3])
        next_state.append(maps[k])

    return offset, next_state

def part_1(input_strings, times=20, maps=dict()):
    initial_state = input_strings.pop(0)
    input_strings.pop(0)
    raw_maps = input_strings[0]

    initial_state = [c == '#' for c in initial_state.replace('initial state: ', '').strip()]
    states = [initial_state]

    for raw_line in raw_maps:
        line = raw_line.split('=>')
        key = tuple(c == '#' for c in line[0].strip())
        maps[key] = '#' in line[1]

    offset = 0
    for _ in range(times):
        ns = get_next_state(states[-1], maps)
        states.append(ns[1])
        offset += ns[0]-2

    s = 0
    for loc, val in enumerate(states[-1]):
        if val:
            s += loc - offset
    return s

test_list = [
        'initial state: #..#.#..##......###...###',
        '',
        ['...## => #',
         '..#.. => #',
         '.#... => #',
         '.#.#. => #',
         '.#.## => #',
         '.##.. => #',
         '.#### => #',
         '#.#.# => #',
         '#.### => #',
         '##.#. => #',
         '##.## => #',
         '###.. => #',
         '###.# => #',
         '####. => #',]]
assert part_1(test_list[:], maps=defaultdict(bool)) == 325, part_1(test_list, maps=defaultdict(bool))

with open('input.txt') as f:
    initial_state = f.readline()
    _ = f.readline()
    raw_maps = f.readlines()

print('Part 1', part_1([initial_state, _, raw_maps]))
print('Part 2(50)', part_1([initial_state, _, raw_maps], times=50))
print('Part 2(500)', part_1([initial_state, _, raw_maps], times=500))
print('Part 2(5000)', part_1([initial_state, _, raw_maps], times=5000))
print('Part 2(50000)', part_1([initial_state, _, raw_maps], times=50000))
print('Part 2(500000)', part_1([initial_state, _, raw_maps], times=500000))

