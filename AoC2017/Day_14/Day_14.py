#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from AoC2017.Day_10.Day_10 import knot_hash
import itertools

def used_squares(s):
    used = 0
    for i in range(128):
        row_string = '{s}-{i}'.format(s=s, i=i) # No f strings yet
        used += bin(int(knot_hash(row_string), 16)).count('1')

    return used


FLAG = -1

def regions(s):
    m = [[None for _ in range(128)] for _ in range(128)]
    # Create the grid
    for row_loc, _ in enumerate(m):
        row_string = '{}-{}'.format(s, row_loc)

        b = bin(int(knot_hash(row_string), 16))[2:]
        for loc, val in enumerate(b.rjust(128, '0')):
            if val == '1':
                m[row_loc][loc] = FLAG

    cnt = 1
    equivalent_regions = {} # max:min
    for row_loc, row in enumerate(m):
        for col_loc, val in enumerate(row):
            if val is None:
                continue

            elif val == FLAG:
                # Start
                q = [(row_loc, col_loc)]

                while q:
                    # Pop
                    n = q.pop()

                    nodes = [n]
                    if n[0] > 0:
                        # Can go north
                        nodes.extend([(n[0]-1, n[1])])

                    if n[0] < len(m)-1:
                        # Can go south
                        nodes.extend([(n[0]+1, n[1])])

                    if n[1] > 0:
                        # Can go west
                        nodes.extend([(n[0], n[1]-1)])

                    if n[1] < len(m[0])-1:
                        # Can go east
                        nodes.extend([(n[0], n[1]+1)])


                    for node in nodes:
                        if m[node[0]][node[1]] == FLAG:
                            m[node[0]][node[1]] = cnt
                            # Spread
                            q.append(node)

                cnt += 1

    return len(set(((i for i in itertools.chain(*m) if i is not None))))


if __name__ == '__main__':
    test_input = 'flqrgnkx'

    assert used_squares(test_input) == 8108

    puzzle_input = 'oundnydw'
    print('Part One:{}'.format(used_squares(puzzle_input)))

    assert regions(test_input) == 1242, '{} != 1242'.format(regions(test_input))

    print('Part Two:{}'.format(regions(puzzle_input)))

