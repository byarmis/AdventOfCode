#!/usr/bin/env python
# -*- coding: utf-8 -*-

def reallocate_mem(b):
    # Get idx of first max
    m = max(b)
    for loc, val in enumerate(b):
        if val == m:
            break

    amt = val
    b[loc] = 0

    # While we have memory, run through, allocating
    while amt > 0:
        loc += 1
        if loc == len(b):
            loc = 0

        b[loc] += 1
        amt -= 1


def reallocate_cycle_count(b):
    seen_configs = {tuple(b),}

    reallocate_mem(b)

    c = 1
    while tuple(b) not in seen_configs:
        seen_configs.add(tuple(b))
        reallocate_mem(b)
        c += 1

    return c, b


if __name__ == '__main__':
    test_bank = [0,2,7,0]

    assert reallocate_cycle_count(test_bank)[0] == 5
    assert reallocate_cycle_count(reallocate_cycle_count(test_bank)[1])[0] == 4

    p = [2, 8, 8, 5, 4, 2, 3, 1, 5, 5, 1, 2, 15, 13, 5, 14]

    p1 = reallocate_cycle_count(p)
    print 'Part one:{}'.format(p1[0])
    print 'Part two:{}'.format(reallocate_cycle_count(p1[1])[0])

