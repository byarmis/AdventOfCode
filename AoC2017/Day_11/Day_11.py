#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple
# axial coordinates
# north to the top right
DIRECTIONS = {
        'n':  (1, -1),
        'ne': (1,  0),
        'se': (0,  1),
        's':  (-1, 1),
        'sw': (-1, 0),
        'nw': (0, -1)
        }


Cube = namedtuple('Cube', ['x', 'y', 'z'])
Hex = namedtuple('Hex', ['q', 'r'])

def axial_to_cube(p):
    return Cube(x=p.q, y=-p.q - p.r, z=p.r)

def cube_distance(a, b):
    return max(abs(a.x - b.x), abs(a.y - b.y), abs(a.z - b.z))

def hex_distance(a, b):
    return cube_distance(axial_to_cube(a), axial_to_cube(b))

def steps(s):
    loc = Hex(q=0, r=0)
    max_distance = 0
    for step in s.strip().split(','):
        loc = Hex(loc.q + DIRECTIONS[step][0],
                  loc.r + DIRECTIONS[step][1])
        dist = hex_distance(loc, Hex(0,0))
        max_distance = max(max_distance, dist)

    return dist, max_distance


if __name__ == '__main__':
    assert steps('ne,ne,ne')[0] == 3
    assert steps('ne,ne,sw,sw')[0] == 0
    assert steps('ne,ne,s,s')[0] == 2
    assert steps('se,sw,se,sw,sw')[0] == 3


    with open('input.txt') as f:
        final_distance, max_distance = steps(f.readline())
        print('Part One:{}\nPart Two:{}'.format(final_distance, max_distance))

