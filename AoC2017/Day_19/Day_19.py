#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string

DIR = { 'U':(-1, 0)
      , 'D':(1,  0)
      , 'L':(0, -1)
      , 'R':(0,  1)
}

INV_DIR = { 'U': 'D'
          , 'D': 'U'
          , 'L': 'R'
          , 'R': 'L'
}

def day_19(filename):
    with open(filename) as f:
            maze = f.read().splitlines()

    letters = []

    vertical = '|'
    horizontal = '-'
    tee = '+'
    
    row = 0
    col = maze[row].index(vertical)

    d = 'D'
    L = maze[row][col]
    steps = 0

    while L != '':
        row += DIR[d][0]
        col += DIR[d][1]

        if row < 0 or col < 0:
            break

        steps += 1
        L = maze[row][col].strip()

        if L and L in string.ascii_uppercase:
            letters.append(L)

        # Turn
        if L == '+':
            for new_dir in DIR.keys() - set(INV_DIR[d]):
                new_row = row + DIR[new_dir][0]
                new_col = col + DIR[new_dir][1]
                try:
                    if maze[new_row][new_col].strip():
                        # It's a valid direction
                        d = new_dir
                        break

                except IndexError:
                    continue
            else:
                raise NotImplementedError

    return letters, steps

if __name__ == '__main__':
    assert day_19('test.txt')[0] == list('ABCDEF'), day_19('test.txt')[0]
    assert day_19('test.txt')[1] == 38, day_19('test.txt')[1]

    print('Part One:{}'.format(''.join(day_19('input.txt')[0])))
    print('Part Two:{}'.format(day_19('input.txt')[1]))
    
