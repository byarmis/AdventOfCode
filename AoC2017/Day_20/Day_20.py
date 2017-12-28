#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from collections import Counter

class Vector:
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

    @property
    def dist(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def __add__(self, other):
        return Vector(self.x + other.x,
                      self.y + other.y,
                      self.z + other.z)
    def __str__(self):
        return '({},{},{})'.format(self.x, self.y, self.z)

class Particle:
    def __init__(self, num, position, velocity, acceleration):
        self.num = num
        self.pos = position
        self.vel = velocity
        self.acc = acceleration

    def __repr__(self):
        return '{} Particle({},{},{})'.format(self.num, self.pos, self.vel, self.acc)

    def tick(self):
        self.vel += self.acc
        self.pos += self.vel

    def __lt__(self, other):
        return self.pos.dist < other.pos.dist
    def __le__(self, other):
        return self.pos.dist <= other.pos.dist
    def __ne__(self, other):
        return self.pos.dist != other.pos.dist
    def __gt__(self, other):
        return self.pos.dist > other.pos.dist
    def __ge__(self, other):
        return self.pos.dist >= other.pos.dist

    def __eq__(self, other):
        return self.pos.x == other.pos.x\
                and self.pos.y == other.pos.y\
                and self.pos.z == other.pos.z


    def __hash__(self):
        return hash((self.pos.x, self.pos.y, self.pos.z))
                

REGEX = r'.*<(.*)>.*<(.*)>.*<(.*)>.*'

def part_1(filename):
    with open(filename) as f:
        f = f.readlines()

    
    particles = []
    for i, line in enumerate(f):
        _, p, v, a, _ = re.split(REGEX, line)

        p = Vector(*p.split(','))
        v = Vector(*v.split(','))
        a = Vector(*a.split(','))

        particles.append(Particle(i, p, v, a))


    closest = min(particles)

    while True:
        for _ in range(1000):
            _ = [p.tick() for p in particles]

            new_closest = min(particles)

            if new_closest is not closest:
                closest = new_closest
                # Closest changed, keep ticking
                break
        else:
            # If we go 1000 cycles without the closest particle chaning, we're good
            break

    return closest

def part_2(filename):
    with open(filename) as f:
        f = f.readlines()
    
    particles = []
    for i, line in enumerate(f):
        _, p, v, a, _ = re.split(REGEX, line)

        p = Vector(*p.split(','))
        v = Vector(*v.split(','))
        a = Vector(*a.split(','))

        particles.append(Particle(i, p, v, a))

    num_particles = len(particles)

    while True:
        for _ in range(10):
            _ = [p.tick() for p in particles]

            cnt = Counter(particles)
            dupes = [p for p, c in cnt.items() if c > 1]

            particles = [p for p in particles if p not in dupes]

            new_num = len(particles)

            if new_num != num_particles:
                num_particles = new_num
                break
        else:
            break
    return num_particles



if __name__ == '__main__':
    tst = part_1('test.txt')
    assert tst.num == 0, tst.num

    print('Part One:{}'.format(part_1('input.txt')))

    tst = part_2('test2.txt')
    assert tst == 1, tst

    print('Part Two:{}'.format(part_2('input.txt')))

