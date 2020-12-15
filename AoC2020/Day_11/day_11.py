from copy import deepcopy

with open('input.txt') as f:
    seats = []
    for i in f.readlines():
        seats.append([j for j in i.strip()])

with open('tst.txt') as f:
    tst = []
    for i in f.readlines():
        tst.append([j for j in i.strip()])


def get_adjacent(seats, pos):
    x,y = pos
    cnt = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                continue
            if x+i < 0 or y+j<0:
                continue

            try:
                if seats[x+i][y+j] == '#':
                    cnt += 1
            except IndexError:
                continue

    return cnt


def part_1(seats):
    changed = True
    while changed:
        changed = False
        new = deepcopy(seats)

        for row in range(len(seats)):
            for col in range(len(seats[row])):
                s = seats[row][col]
                if s == '.':
                    continue

                c = get_adjacent(seats, (row, col))
                if  s == 'L' and c == 0:
                    new[row][col] = '#'
                    changed = True
                elif s == '#' and c >= 4:
                    new[row][col] = 'L'
                    changed = True

        seats = deepcopy(new)

    return sum(row.count('#') for row in seats)

assert part_1(tst) == 37, part_1(tst)

print('part 1: ', part_1(seats))

def get_seen(seats, pos):

    cnt = 0
    for x_dir in range(-1, 2):
        for y_dir in range(-1, 2):
            if x_dir == y_dir == 0:
                continue

            i, j = pos
            i += x_dir
            j += y_dir
            try:
                while seats[i][j] == '.':
                    i += x_dir
                    j += y_dir

                    if i < 0 or j < 0:
                        break

                if i>=0 and j>=0 and seats[i][j] == '#':
                    cnt += 1

            except IndexError:
                continue

    return cnt


def part_2(seats):
    changed = True
    while changed:
        changed = False
        new = deepcopy(seats)

        for row in range(len(seats)):
            for col in range(len(seats[row])):
                s = seats[row][col]
                if s == '.':
                    continue

                c = get_seen(seats, (row, col))
                if  s == 'L' and c == 0:
                    new[row][col] = '#'
                    changed = True
                elif s == '#' and c >= 5:
                    new[row][col] = 'L'
                    changed = True

        seats = deepcopy(new)

    return sum(row.count('#') for row in seats)


assert part_2(tst) == 26, part_2(tst)

print('part 2: ', part_2(seats))


