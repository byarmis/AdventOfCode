#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import product

class Array:
    def __init__(self, a):
        if isinstance(a, str):
            self._a = self.process_string(a)
        elif isinstance(a, Array):
            return a
        else:
            self._a = a

        self.cnt = sum(sum(i) for i in self._a)
        self.hash = hash(tuple(tuple(i) for i in self._a))

    def __hash__(self):
        return self.hash

    def __len__(self):
        return len(self._a)

    @staticmethod
    def process_string(string):
        return [[j=='#' for j in i.strip()] for i in string.split('/')]

    def __repr__(self):
        return '\n'.join(str(a) for a in self._a)

    def __eq__(self, other):
        if len(self) != len(other):
            return False

        if self.cnt != other.cnt:
            return False

        if hash(self) != hash(other):
            return False

        for i in range(len(self._a)):
            for j in range(len(self._a[0])):
                if self._a[i][j] != other._a[i][j]:
                    return False

        return True

    @property
    def mirror(self): 
        return Array([i[::-1] for i in self._a])

    @property
    def reverse(self):
        return Array(self._a[::-1])

    @property
    def rotate(self):
        # Column index becomes the row index
        # abs(Row index - len) becomes the col index
        o = [[None for _ in self._a[0]] for _ in self._a]
        assert len(o) == len(o[0])

        for row_idx, row in enumerate(self._a):
            for col_idx, val in enumerate(row):
                o[col_idx][abs(row_idx - len(self) + 1)] = val

        return Array(o)

    def __getitem__(self, x):
        return self._a[x]


class Grid:
    def __init__(self, inp):
        self.array = Array(inp)

        self.perms = None
        self.generate_permutations()

    def __repr__(self):
        return self.array.__repr__()

    def __len__(self):
        return len(self.array)

    def __hash__(self):
        return hash(self.array)

    def generate_permutations(self):
        perms = [self.array] # Normal
        a = self.array

        # Go through the 3 rotations
        for _ in range(3):
            # Append the rotation, its mirror, its reverse, and its mirror reverse
            perms.append(a)
            perms.append(a.reverse)
            perms.append(a.mirror)
            perms.append(a.mirror.reverse)

            a = a.rotate
        
        self.perms = tuple(perms)

    def __eq__(self, other):
        if self.cnt != other.cnt:
            return False

        for s, o in product(self.perms, other.perms):
            if s == o:
                return True

        return False

    def __getitem__(self, x):
        return self.array[x]

    @property
    def cnt(self):
        return self.array.cnt

class Art:
    def __init__(self, d):
        self.grid = Grid('.#./..#/###')
        self.size = len(self.grid)
        self.enhancement_dict = d

    @property
    def on_count(self):
        return self.grid.cnt

    def grow(self):
        if self.size % 2 == 0:
            n = 2
            self.size *= 3/2

        elif self.size % 3 == 0:
            n = 3
            self.size *= 4/3

        else:
            raise NotImplementedError

        def split(grid):
            row_start = 0
            sub_arrays = []

            # Split into subgrids
            while row_start < len(grid):
                col_start = 0
                row = []
                while col_start < len(grid):
                    new_subgrid = [x[col_start:col_start+n] for x in grid[row_start:row_start+n]]

                    row.append(Grid(new_subgrid))
                    col_start += n

                sub_arrays.append(row)

                row_start += n

            return sub_arrays

        def _grow(sub_arrays):
            # Grow the subgrids
            new_arrays = []
            for row in sub_arrays:
                new_row = []

                for array in row:
                    for k, v in self.enhancement_dict.items():
                        if array == k:
                            new_row.append(v)
                            break
                    else:
                        raise AssertionError('No enhancement found')

                new_arrays.append(new_row)

            return new_arrays

        def merge(new_arrays):
            # Merge the subgrids
            # Join everything back together

            new_grid = []
            big_row = 0

            for big_row in new_arrays:
                # Get the Nth row of each subgrid
                n = 0
                while n < len(big_row[0]):
                    new_row = []
                    for subgrid in big_row:
                        new_row.extend(subgrid[n])
                    new_grid.append(new_row)
                    n += 1
            return Grid(new_grid)


        sub_arrays = split(self.grid)
        new_arrays = _grow(sub_arrays)
        new_grid   = merge(new_arrays)

        self.grid = new_grid

def get_enhancement_dict(filename):
    with open(filename) as f:
        f = f.read().splitlines()
    out = {}
    for line in f:
        k, v = line.split('=>')
        out[Grid(k)] = Grid(v)
    return out

if __name__ == '__main__':
    g1 = Grid('.#./..#/###')
    g2 = Grid('.#./#../###')
    g3 = Grid('#../#.#/##.')
    g4 = Grid('###/..#/.#.')

    assert g1 == g2 == g3 == g4

    ed = get_enhancement_dict('test.txt')

    a = Art(ed)
    a.grow()
    a.grow()

    assert a.on_count == 12, 'On-count must be 12'

    ed = get_enhancement_dict('input.txt')
    a = Art(ed)
    for _ in range(5):
        a.grow()

    print('5 iterations', a.on_count)

    a = Art(ed)

    for i in range(18):
        print(i)
        a.grow()

    print('18 iterations', a.on_count)

