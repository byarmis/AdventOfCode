import re 

LEFT = {
        'E': 'N',
        'N': 'W',
        'W': 'S',
        'S': 'E'
        }

RIGHT = {
        'E': 'S',
        'S': 'W',
        'W': 'N',
        'N': 'E'
        }

with open('input.txt') as f:
    dirs = f.readlines()

with open('tst.txt') as f:
    tst = f.readlines()

def part_1(dirs):
    def move(pos, D, A):
        if D == 'N':
            pos[1] += A
        elif D == 'S':
            pos[1] -= A
        elif D == 'E':
            pos[0] += A
        elif D == 'W':
            pos[0] -= A
        else:
            raise ValueError(f'Unknown direction: {D}')
        return pos


    direction = 'E'
    pos = [0,0]
    for d in dirs:
        D, A = re.findall(r'([A-Z])(.*)', d)[0]
        A = int(A)
        if D in {'N', 'S', 'E', 'W'}:
            pos = move(pos, D, A)
            continue

        if D == 'F':
            pos = move(pos, direction, A)
        elif D == 'L':
            while A:
                direction = LEFT[direction]
                A -= 90

        elif D == 'R':
            while A:
                direction = RIGHT[direction]
                A -= 90

    return sum(abs(a) for a in pos)


assert part_1(tst) == 25, part_1(tst)
print('part 1: ', part_1(dirs))


def part_2(dirs):
    def move_wp(wp, A):
        if D == 'N':
            wp[1] += A

        elif D == 'S':
            wp[1] -= A

        elif D == 'E':
            wp[0] += A

        elif D == 'W':
            wp[0] -= A

        else:
            raise ValueError(f'Unknown direction: {D}')
        return wp
    def mat_mult(x, y):
        a, b = x[0]
        c, d = x[1]
        i, s = y

        return [a*i + b*s, c*i + d*s]

    direction = 'E'
    pos = [0,0]
    wp = [10, 1]

    for d in dirs:
        D, A = re.findall(r'([A-Z])(.*)', d)[0]
        A = int(A)
        if D in {'N', 'S', 'E', 'W'}:
            wp = move_wp(wp, A)
            continue

        if D == 'F':
            pos[0] += wp[0] * A
            pos[1] += wp[1] * A

        elif D == 'L':
            m = [[0, -1], [1, 0]]
            while A:
                wp = mat_mult(m, wp)
                direction = LEFT[direction]
                A -= 90

        elif D == 'R':
            m = [[0, 1], [-1, 0]]

            while A:
                wp = mat_mult(m, wp)
                direction = RIGHT[direction]
                A -= 90

    return sum(abs(a) for a in pos)


assert part_2(tst) == 286, part_2(tst)
print('part 2: ', part_2(dirs))

