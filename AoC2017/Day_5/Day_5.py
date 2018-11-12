#!/usr/bin/env python
# -*- coding: utf-8 -*-

def jumps_to_exit(j, f):
    i = 0
    c = 0

    while 0 <= i < len(j):
        to_jump = j[i]
        j[i] += f(j[i])

        i += to_jump
        c += 1

    return c

if __name__ == '__main__':
    test_list = [0, 3, 0, 1, -3]

    part_one = lambda x: 1
    part_two = lambda x: -1 if x >= 3 else 1

    assert jumps_to_exit(test_list[:], part_one) == 5, 'Part One failed'
    assert jumps_to_exit(test_list[:], part_two) == 10, 'Part Two failed'

    with open('input.txt') as f:
        list_in = [int(i) for i in f.readlines()]

    print('Part One:{}'.format(jumps_to_exit(list_in[:], part_one)))

    print('Part Two:{}'.format(jumps_to_exit(list_in[:], part_two)))

