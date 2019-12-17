#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import cycle, dropwhile, repeat


def limited_cycle(iterable, limit):
    for _ in range(limit):
        yield from iterable

def ones(i):
    return int(str(i)[-1])

def fft_round(signal, repeat):
    output = 0
    i = repeat - 1
    while i < len(signal):
        for _ in range(repeat):
            try:
                output += signal[i]
            except IndexError:
                break
            i += 1
        i += repeat * 3

    i = 3*repeat -1
    while i < len(signal):
        for _ in range(repeat):
            try:
                output -= signal[i]
            except IndexError:
                break

            i += 1
        i += repeat * 3

    return ones(output)

def fft(signal):
    return [fft_round(signal, i) for i in range(1, len(signal)+1 )]

if __name__ == '__main__':
    r = fft([1,2,3,4,5,6,7,8,]) 
    assert r == [4,8,2,2,6,1,5,8,], r

    with open('input.txt') as f:
        signal = [int(i) for i in f.readline().strip()]

    for _ in range(100):
        signal = fft(signal)

    print(f"Part 1:{''.join(str(i) for i in signal[:8])}")

    with open('input.txt') as f:
        signal = [int(i) for i in f.readline().strip()]

    offset = int(''.join(str(s) for s in signal[:7]))
    signal = list(limited_cycle(signal, 10000))
    for i in range(100):
        print(i)
        signal = fft(signal)

    s, e = offset, offset + 9
    print(f"Part 2:{''.join(str(i) for i in signal[s:e])}")

