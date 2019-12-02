#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def part_1(program):
    i = 0
    while i < len(program):
        opcode, a, b, dest = program[i:i+4]
        i += 4

        assert opcode in {1, 2, 99}, f'Unexpected opcode: {opcode}'

        if opcode == 1:
            val = program[a] + program[b]
        elif opcode == 2:
            val = program[a] * program[b]
        elif opcode == 99:
            return program

        program[dest] = val

def part_2(program, goal):
    for noun in range(99):
        for verb in range(99):
            p = program[:]
            p[1] = noun
            p[2] = verb

            p = part_1(p)
            if p[0] == goal:
                return noun, verb

if __name__ == '__main__':
    with open('input.txt') as f:
        program = f.readline()
    program = [int(i) for i in program.split(',')]
    p_1 = program[:]
    p_1[1] = 12
    p_1[2] = 2
    p = part_1(p_1)
    print(f'part 1: {p[0]}')
    noun, verb = part_2(program, 19690720)
    print(f'part 2: noun={noun}\n\tverb={verb}')

