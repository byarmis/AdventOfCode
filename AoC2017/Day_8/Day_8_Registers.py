#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections

def compare(register, symbol, value, registers):
    string = '{} {} {}'.format(registers[register], symbol, int(value.strip()))

    return eval(string)

def day_8(filename):
    with open(filename) as f:
        lines = f.readlines()

    directions = {'inc': lambda x: x, 'dec': lambda x: -1 * x}
    registers = collections.defaultdict(int)

    max_ever = 0

    for line in lines:
        register, direction, amt, *cond = line.split(' ')

        if compare(register=cond[1], symbol=cond[2], value=cond[3], registers=registers):
            registers[register] += directions[direction](int(amt))
            max_ever = max(max(registers.values()), max_ever)

    return max(registers.values()), max_ever

if __name__ == '__main__':
    day_8('test.txt') == 1
    
    print(day_8('input.txt'))

