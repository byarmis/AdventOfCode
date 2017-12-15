#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    i = 0
    with open('input.txt') as f:
        for line in f.readlines():
            pw = line.strip().split(' ')
            if len(pw) == len(set(pw)):
                i += 1

    print('Part One:{}'.format(i))

    i = 0
    with open('input.txt') as f:
        for line in f.readlines():
            pw = [''.join(sorted(list(w))) for w in line.strip().split(' ')]
            if len(pw) == len(set(pw)):
                i += 1

    print('Part Two:{}'.format(i))

