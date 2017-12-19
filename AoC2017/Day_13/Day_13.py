#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict

def scanner(max_depth, t):
    if max_depth > 0:
        max_depth -= 1
        return abs(((t-max_depth) % (max_depth * 2)) - max_depth) == 0

def get_firewall_dict(filename):
    d = defaultdict(int)

    with open(filename) as f:
        for line in f:
            key, value = line.split(':')

            d[int(key)] = int(value)

    return d

def get_cost(firewall, cur, delay=0):
    if scanner(firewall[cur], cur+delay):
        return firewall[cur] * cur
    return 0

def part_1(filename):
    firewall = get_firewall_dict(filename)

    cost = 0
    for i in range(max(firewall.keys())+1):
        cost += get_cost(firewall, i)
        
    return cost
    
def part_2(filename):
    firewall = get_firewall_dict(filename)

    delay = 0
    while True:
        for i in range(max(firewall.keys())+1):
            if scanner(firewall[i], i+delay):
                break
        else:
            return delay

        delay += 1


    
if __name__ == '__main__':
    t1 = part_1('test.txt')
    t2 = part_2('test.txt')

    assert t1 == 24, 'Expected:24, Actual:{}'.format(t1)
    assert t2 == 10, 'Expected:10, Actual:{}'.format(t2)

    print('Part One:{}'.format(part_1('input.txt')))
    print('Part Two:{}'.format(part_2('input.txt')))


