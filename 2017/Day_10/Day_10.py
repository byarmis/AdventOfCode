#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools
from operator import xor

def knot_hash_round(i, length, repeat=1):
    string = list(range(length))
    cur = 0
    skip_size = 0

    for _ in range(repeat):
        for val in i:
            # Get sublist
            if cur + val < length:
                # No wraparaound
                sublist = string[cur:cur+val]
            else:
                leftover = (cur + val) - length
                sublist = string[cur:] + string[:leftover]

            # Reverse sublist
            sublist = sublist[::-1]

            for sublist_idx, value in enumerate(sublist):
                idx = sublist_idx + cur
                idx %= length

                string[idx] = value

            cur += skip_size + len(sublist)
            cur %= length

            skip_size += 1

    return string

def blocker(iterable, n=16):
    args = [iter(iterable)] * n
    return itertools.izip_longest(*args)

def knot_hash(str_in):
    suffix = [17, 31, 73, 47, 23]
    lengths = [ord(i) for i in str_in] + suffix

    current_position = 0
    skip_size = 0

    sparse_hash = knot_hash_round(lengths, 256, repeat=64)

    dense_hash = [reduce(xor, block) for block in blocker(sparse_hash)]

    return ''.join('{:02x}'.format(i) for i in dense_hash)


if __name__ == '__main__':
    test_len = 5
    test_input = [3, 4, 1, 5]

    test_output = knot_hash_round(test_input, test_len)
    assert test_output[0] * test_output[1] == 12

    actual_len = 256
    actual_input = [14,58,0,116,179,16,1,104,2,254,167,86,255,55,122,244]

    output = knot_hash_round(actual_input, actual_len)
    print('Part One:{}'.format(output[0] * output[1]))

    assert output[0] * output[1] == 1935

    assert knot_hash('') == 'a2582a3a0e66e6e86e3812dcb672a272'
    assert knot_hash('1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d'
    assert knot_hash('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
    assert knot_hash('1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e'

    puzzle_input = '14,58,0,116,179,16,1,104,2,254,167,86,255,55,122,244'
    print('Part Two:{}'.format(knot_hash(puzzle_input)))

