
def part_1(depth, target):
    tx, ty = target
    c = [[None for _ in range(ty+1)] for _ in range(tx+1)]
    c[0][0] = 0
    c[tx][ty] = 0

    def erosion(x, y):
        if c[x][y] is not None:
            pass

        elif y == 0:
            c[x][y] = x * 16807

        elif x == 0:
            c[x][y] = y * 48271

        else:
            c[x][y] = erosion(x-1, y) * erosion(x, y-1)

        return (c[x][y] + depth) % 20183

    return sum(erosion(x,y) % 3 for x in range(tx+1) for y in range(ty+1))

test = part_1(depth=510, target=(10,10))
assert test == 114, test

print(part_1(depth=11817, target=(9, 751)))

