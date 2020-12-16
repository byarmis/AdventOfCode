import re
from collections import defaultdict

def mask(m, v):
    v = int(v)
    for loc, val in enumerate(m[::-1]):
        if val == 'X':
            continue
        else:
            v ^= (-int(val) ^ v) & (1 << loc)

    return v


def part_1(pgm):
    mem = defaultdict(int)
    for line in pgm:
        if line.startswith('mask'):
            m = line.split('=')[1].strip()

        else:
            loc = int(re.findall(r'\[(.*)\].*', line)[0])
            val = line.split('=')[1].strip()
            
            mem[loc] = mask(m, val)

    return sum(mem.values())

with open('input.txt') as f:
    pgm = f.readlines()

with open('tst.txt') as f:
    tst = f.readlines()

assert part_1(tst) == 165, part_1(tst)
print('part 1: ', part_1(pgm))

def possible_vals(val, M):
    val = bin(int(val))[2:].zfill(len(M))
    x_cnt = M.count('X')

    for j in range(2**x_cnt):
        x_used = 0
        a = []
        for v, m in zip(val, M):
            if m == '0':
                a.append(v)
            elif m == '1':
                a.append(1)
            elif m == 'X':
                a.append((j >> x_used) & 1)
                x_used += 1

        yield int(''.join(str(i) for i in a), 2)


def part_2(pgm):
    mem = defaultdict(int)
    for line in pgm:
        if line.startswith('mask'):
            m = line.split('=')[1].strip()

        else:
            loc = int(re.findall(r'\[(.*)\].*', line)[0])
            val = line.split('=')[1].strip()

            for L in possible_vals(loc, m):
                mem[L] = int(val)

    return sum(mem.values())

with open('tst2.txt') as f:
    tst = f.readlines()

assert part_2(tst) == 208, part_2(tst)
print('part two: ', part_2(pgm))

