#!/usr/bin/env python
# -*- coding: utf-8 -*-

def spin(line, n):
    return line[-n:] + line[:-n]

def exchange(line, a, b):
    L = line[:]
    L[a], L[b] = L[b], L[a]

    return L

def partner(line, a, b):
    a = line.index(a)
    b = line.index(b)

    return exchange(line, a, b)

def dance(line, inst):
    if inst[0] == 's':
        line = spin(line, int(inst[1:]))

    elif inst[0] == 'x':
        a, b = inst[1:].split('/')
        line = exchange(line, int(a), int(b))

    elif inst[0] == 'p':
        a, b = inst[1:].split('/')
        line = partner(line, a, b)

    return line

def DANCE(LINE, filename):
    with open(filename) as f:
        instructions = f.readline()

    LINE = list(LINE)
    for i in instructions.strip().split(','):
        LINE = dance(LINE, i)

    return LINE


if __name__ == '__main__':

    test_line = list('abcde')
    for i in ['s1', 'x3/4','pe/b']:
        test_line = dance(test_line, i)

    assert ''.join(test_line) == 'baedc', test_line

    LINE = DANCE('abcdefghijklmnop', 'input.txt')
    print('Part One:{}'.format(''.join(LINE)))

    # Find cycle
    seen = list()
    billion = 1000000000
    LINE = 'abcdefghijklmnop'

    for i in range(billion):
        LINE = DANCE(LINE, 'input.txt')
        if LINE in seen:
            break
        seen.append(LINE)

    print('Part Two:{}'.format(''.join(seen[(billion % i)-1])))

