#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import zip_longest
from collections import deque

def intcode(program, input_queue):

    i = 0
    ret_val = None

    while i < len(program):
        instruction = program[i] 
        i += 1
        if instruction == 99:
            return ret_val

        opcode = instruction % 10
        assert opcode in range(1,9), f'Unexpected opcode: {opcode}'

        instruction = str(instruction)[0:-2]

        # One code
        if opcode in {3,4}:
            a = program[i]
            mode = instruction[0] if instruction else 0

            if opcode == 3:
                if ret_val is not None:
                    raise ValueError('Multiple inputs found')
                program[a] = input_queue.popleft()

            elif opcode == 4:
                v = a if mode else program[a]
                if v != 0:
                    ret_val = v

            i += 1

        # Two code
        elif opcode in {5,6}:
            a, b = program[i:i+2]
            modes = {}
            for mode in zip_longest(instruction[::-1], ['a','b'], fillvalue=0):
                modes[mode[1]] = int(mode[0])

            A = a if modes['a'] else program[a]
            B = b if modes['b'] else program[b]

            if (opcode == 5 and A != 0) or (opcode == 6 and A == 0):
                i = B
            else:
                i += 2

        # Three code
        else:
            a, b, dest = program[i:i+3]
            modes = {}
            for mode in zip_longest(instruction[::-1], ['a','b','dest'], fillvalue=0):
                modes[mode[1]] = int(mode[0])

            A = a if modes['a'] else program[a]
            B = b if modes['b'] else program[b]

            if opcode == 1:
                val = A + B
            elif opcode == 2:
                val = A * B
            elif opcode == 7:
                if A < B:
                    val = 1
                else:
                    val = 0
            elif opcode == 8:
                if A == B:
                    val = 1
                else:
                    val = 0

            program[dest] = val
            i += 3

    if ret_val is not None:
        return ret_val
    else:
        raise ValueError('Reached the end of the program')

if __name__ == '__main__':
    with open('input.txt') as f:
        program = f.readline()
    program = [int(i) for i in program.split(',')]

    r = intcode([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], deque([7]))
    assert r == 999, r

    r = intcode([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], deque([8]))
    assert r == 1000, r

    r = intcode([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], deque([9]))
    assert r == 1001, r


    print(f'Part 1: {intcode(program[:], deque([1]))}')
    print(f'Part 2: {intcode(program[:], deque([5]))}')

