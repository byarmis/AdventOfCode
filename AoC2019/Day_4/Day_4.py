#!/usr/bin/env python
# -*- coding: utf-8 -*-

def has_double(num):
    num = str(num)
    for pair in zip(num, num[1:]):
        if pair[0] == pair[1]:
            return True
    return False

def only_increase(num):
    num = str(num)
    for pair in zip(num, num[1:]):
        if int(pair[1]) < int(pair[0]):
            return False
    return True

def doubles_part_of_larger(num):
    num = str(num)
    min_length = float('inf')
    loc = 0

    while loc < len(num):
        val = num[loc]
        # Go along until the dupes end
        t_loc = loc
        while  t_loc < len(num) and num[t_loc] == val:
            t_loc += 1
        length = t_loc - loc
        loc = t_loc
        if length >= 2:
            min_length = min((length, min_length))

    return min_length != 2

def part_1(num):
    if not has_double(num):
        return False
    if not only_increase(num):
        return False
    return True

def part_2(num):
    if not has_double(num):
        return False
    if not only_increase(num):
        return False
    if doubles_part_of_larger(num):
        return False
    return True

def is_valid(func, low, high):
    for num in range(low, high+1):
        if func(num):
            yield num
        else:
            continue

if __name__ == '__main__':
    assert part_1(111111)
    assert not part_1(223450)
    assert not part_1(123789)

    matches = is_valid(part_1, 246540, 787419)
    print(f'Part one: {len(list(matches))}')

    assert part_2(112233) 
    assert not part_2(123444)
    assert part_2(111122)

    matches = is_valid(part_2, 246540, 787419)
    print(f'Part two: {len(list(matches))}')

