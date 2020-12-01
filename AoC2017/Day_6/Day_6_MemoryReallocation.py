#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import namedtuple

def reallocate_mem(bank):
    # Get idx of first max
    amt = max(bank)
    idx = bank.index(amt)

    bank[idx] = 0

    # While we have memory, run through, allocating
    while amt > 0:
        idx += 1
        idx %= len(bank) # Wrap around

        bank[idx] += 1
        amt -= 1

def reallocate_cycle_count(bank):
    seen_configs = set()
    count = 0

    while tuple(bank) not in seen_configs:
        seen_configs.add(tuple(bank))
        reallocate_mem(bank)
        count += 1

    return namedtuple('result', 'count final_val')(count, bank)


if __name__ == '__main__':
    test_bank = [0,2,7,0]

    assert reallocate_cycle_count(test_bank).count == 5
    assert reallocate_cycle_count(reallocate_cycle_count(test_bank).final_val).count == 4

    p = [2, 8, 8, 5, 4, 2, 3, 1, 5, 5, 1, 2, 15, 13, 5, 14]

    res = reallocate_cycle_count(p)
    print('Part one:{}'.format(res.count))
    print('Part two:{}'.format(reallocate_cycle_count(res.final_val).count))

