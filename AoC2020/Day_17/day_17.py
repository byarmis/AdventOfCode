from copy import deepcopy
from collections import defaultdict

with open('input.txt') as f:
    inp = f.readlines()

with open('tst.txt') as f:
    tst = f.readlines()

def get_dim(inp, d):
    dim = defaultdict(bool)
    for row_num, row in enumerate(inp):
        for col_num, col in enumerate(row.strip()):
            if d == 3:
                dim[(row_num, col_num, 0)] = col == '#'
            elif d == 4:
                dim[(row_num, col_num, 0, 0)] = col == '#'

    return dim

def three_neighbors(c):
    X, Y, Z = c
    for x in range(X-1, X+2):
        for y in range(Y-1, Y+2):
            for z in range(Z-1, Z+2):
                if x == X and y == Y and z == Z:
                    continue
                yield (x, y, z)

def four_neighbors(c):
    X, Y, Z, W = c
    for x in range(X-1, X+2):
        for y in range(Y-1, Y+2):
            for z in range(Z-1, Z+2):
                for w in range(W-1, W+2):
                    if x == X and y == Y and z == Z and w == W:
                        continue
                    yield (x, y, z, w)


def active_neighbors(dim, c, n_func):
    cnt = 0
    for n in n_func(c):
        if dim[n]:
            cnt += 1
    return cnt


def loop(dim, d):
    if d == 3:
        n_func = three_neighbors
    elif d == 4:
        n_func = four_neighbors

    # Spread
    items = list(dim.items())
    new = deepcopy(dim)

    for cell, is_active in items:
        if is_active:
            for n in n_func(cell):
                new[n] = dim[n]

    # Do logic
    items = list(dim.items())
    for cell, is_active in items:
        if is_active and not (2 <= active_neighbors(dim, cell, n_func) <= 3):
            new[cell] = False
        if not is_active and active_neighbors(dim, cell, n_func) == 3:
            new[cell] = True

    return new

def part_1(inp):
    dim = get_dim(inp, 3)
    for _ in range(6):
        dim = loop(dim, 3)

    return sum(dim.values())

assert part_1(tst) == 112, part_1(tst)

def part_2(inp):
    dim = get_dim(inp, 4)
    for _ in range(6):
        dim = loop(dim, 4)

    return sum(dim.values())


print('part one', part_1(inp))
print('part two', part_2(inp))



