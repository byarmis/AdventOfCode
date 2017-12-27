#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

def duet(f):
    r = defaultdict(int)
    ptr = 0
    sound = None

    while True:
        try:
            inst, reg, val = f[ptr].split(' ')
        except ValueError:
            inst, val = f[ptr].split(' ')

        val = val.strip()
        try:
            v = int(val)
        except ValueError:
            v = r[val]


        if inst == 'set':
            r[reg] = v

        elif inst == 'add':
            r[reg] += v

        elif inst == 'mul':
            r[reg] *= v

        elif inst == 'mod':
            r[reg] %= v

        elif inst == 'jgz':
            if r[reg] > 0:
                ptr += int(val)
                continue

        elif inst == 'snd':
            sound = r[reg]

        elif inst == 'rcv':
            if r[reg] != 0:
                return sound

        ptr += 1


class Thread:
    def __init__(self, n, instructions):
        self._r = defaultdict(int) 
        self._r['p'] = n
        self._ptr = 0
        self._n = n

        self.instructions = instructions

        self.queue = []
        self.send_count = 0

    def send(self, v):
        # send TO this thread
        self.queue.append(v)

    def process(self, other):
        if self._ptr == len(self.instructions):
            return None

        instruction = self.instructions[self._ptr]
        try:
            inst, reg, val = instruction.split(' ')
        except ValueError:
            inst, val = instruction.split(' ')

        val = val.strip()
        try:
            v = int(val)
        except ValueError:
            v = self._r[val]

        if inst == 'set':
            self._r[reg] = v

        elif inst == 'add':
            self._r[reg] += v

        elif inst == 'mul':
            self._r[reg] *= v

        elif inst == 'mod':
            self._r[reg] %= v

        elif inst == 'jgz':
            try:
                if int(reg) > 0:
                    self._ptr += v
                else:
                    self._ptr += 1
            except ValueError:
                if self._r[reg] > 0:
                    self._ptr += v
                else:
                    self._ptr += 1
            return 0

        elif inst == 'snd':
            self.send_count += 1
            other.send(v)

        elif inst == 'rcv':
            if self.queue:
                p = self.queue.pop(0)
                self._r[val.strip()] = p

            else:
                return None

        self._ptr += 1
        return 0


def part_2(filename):
    with open(filename) as f:
        f = f.readlines()

    prog_0 = Thread(0, f)
    prog_1 = Thread(1, f)
    o0 = o1 = 1

    while o0 is not None or o1 is not None:
        o0 = prog_0.process(prog_1)
        o1 = prog_1.process(prog_0)

    return prog_1.send_count


if __name__ == '__main__':
    r = {}

    with open('test.txt') as f:
        f = f.readlines()

    assert duet(f) == 4, duet(f)

    with open('input.txt') as f:
        f = f.readlines()

    print('Part One:{}'.format(duet(f)))
    p2 = part_2('test2.txt')
    assert p2 == 3, p2

    p2 = part_2('input.txt')
    print('Part Two:{}'.format(p2))

