#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def spinlock(i, s, sl=[0]):
    ptr = 0

    for c in range(1, s+1):
        # Step
        ptr += i
        ptr %= len(sl)

        # Insert value
        sl.insert(ptr + 1, c)
        ptr += 1

    return sl

def fast_spin(i,  r):
    ptr = 0
    v = 0
    for step in range(1, r+1):
        ptr = (ptr + i) % step

        if not ptr:
            v = step

        ptr += 1
    return v


def one_after_spinlock(i, search_val=2017):
    sl = spinlock(i, search_val)

    return sl[sl.index(search_val) + 1]

if __name__ == '__main__':
    test_input = 3

    assert one_after_spinlock(test_input) == 638

    actual_input = 344
    print('Part One:{}'.format(one_after_spinlock(actual_input)))
    print('Part Two:{}'.format(fast_spin(actual_input, 50000000)))


    

