from collections import defaultdict
from copy import deepcopy

class Island:
    def __init__(self, lines):
        self.rows = [list(l.strip()) for l in lines.split('\n') if l.strip()]
        transposed = defaultdict(list)
        for line in self.rows:
            for loc, val in enumerate(line):
                if val.strip():
                    transposed[loc].append(val.strip())
        self.columns = [c[1] for c in sorted(list((k,v) for k, v in transposed.items()))]

        self._mirror_type = -1
        self._mirror_type = self.mirror_type()

    def is_mirror_row(self, idx):
        is_mirror = self._is_mirror(self.rows, idx)
        if is_mirror:
            self._mirror_type = ('row', idx)
        return is_mirror


    def is_mirror_column(self, idx):
        is_mirror = self._is_mirror(self.columns, idx)
        if is_mirror:
            self._mirror_type = ('col', idx)

        return is_mirror

    def find_mirror_col(self):
        for c in range(len(self.columns)-1):
            if self.is_mirror_column(c):
                return c

        raise ValueError


    def find_mirror_row(self):
        for r in range(len(self.rows)-1):
            if self.is_mirror_row(r):
                return r

        raise ValueError

    @staticmethod
    def _is_mirror(arr, idx):
        A = arr[idx+1:]
        B = arr[:idx+1][::-1]

        if not A or not B:
            return False

        for a, b in zip(A, B):
            if a != b:
                return False

        return True

    def __repr__(self):
        out_rows = []
        #first_row = [' '] * 3 + [str(i+1) for i in range(len(self.rows[0]))] + [' ']*3
        second_row = [' '] * 3 + [' ']*len(self.rows[0]) + [' ']*3
        if self._mirror_type is not None and self._mirror_type[0] == 'col':
            second_row[self._mirror_type[1]+3] = '>'
            second_row[self._mirror_type[1]+4] = '<'

        #out_rows.append(''.join(first_row))
        out_rows.append(''.join(second_row))
        for i, row in enumerate(self.rows):
            if self._mirror_type == ('row', i):
                mirror_symbol = 'v'
            elif self._mirror_type == ('row', i-1):
                mirror_symbol = '^'
            else:
                mirror_symbol =' '
            out_rows.append(f"{i+1:02d}{mirror_symbol}{''.join(row)}{mirror_symbol}{i+1:02d}")

        out_rows.append(''.join(second_row))
        #out_rows.append(''.join(first_row))
        
        return '\n'.join(out_rows)

    def __eq__(self, other):
        return self.rows == other.rows

    def mirror_type(self):
        if self._mirror_type != -1:
            return self._mirror_type

        try:
            c = self.find_mirror_col()
            self._mirror_type = ('col', c)

            return self._mirror_type

        except ValueError:
            pass

        try:
            r = self.find_mirror_row()
            self._mirror_type = ('row', r)

            return self._mirror_type

        except ValueError:
            self._mirror_type = None

        return self._mirror_type

    def find_mirror_cols(self):
        for c in range(len(self.columns)-1):
            if self.is_mirror_column(c):
                yield c

        raise ValueError


    def find_mirror_rows(self):
        for r in range(len(self.rows)-1):
            if self.is_mirror_row(r):
                yield r

        raise ValueError


    def potential_mirror_types(self):
        try:
            yield from (('row', r) for r in self.find_mirror_rows())
        except ValueError:
            pass
        try:
            yield from (('col', c) for c in self.find_mirror_cols())
        except ValueError:
            pass
        return


    def find_alternate(self):
        for x, row in enumerate(self.rows):
            for y, char in enumerate(row):
                row_copy = deepcopy(self.rows)
                row_copy[x][y] = '#' if row_copy[x][y] == '.' else '.'
                new_rows='\n'.join(''.join(a for a in b) for b in row_copy)
                new_island = Island(new_rows)

                for mt in new_island.potential_mirror_types():
                    if self.mirror_type() == mt:
                        continue


                    print('-'*20)
                    print(self)
                    print(new_island)

                    return new_island

        raise ValueError('idk')


with open('input.txt') as f:
    lines = f.read()


def part_1(lines):
    islands = [Island(line) for line in lines.split('\n\n')]
    summary = 0

    for island in islands:
        try:
            summary += 100*(island.find_mirror_row() + 1)
        except ValueError:
            summary += island.find_mirror_col() + 1

    return summary

def part_2(lines):
    summary = 0

    for island in lines.split('\n\n'):
        original_island = Island(island)
        new_island = original_island.find_alternate()

        try:
            summary += 100*(new_island.find_mirror_row() + 1)
        except ValueError:
            summary += new_island.find_mirror_col() + 1

    return summary


test_lines = '''
    #.##..##.
    ..#.##.#.
    ##......#
    ##......#
    ..#.##.#.
    ..##..##.
    #.#.##.#.

    #...##..#
    #....#..#
    ..##..###
    #####.##.
    #####.##.
    ..##..###
    #....#..#
'''

t = part_1(test_lines)
assert  t == 405, t

print('Part 1: ', part_1(lines))

t = part_2(test_lines)
assert t == 400, t

t = part_2(lines)
assert t < 39517
print('Part 2: ', t)

