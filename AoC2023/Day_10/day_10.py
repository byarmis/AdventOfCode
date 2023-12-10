import itertools

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

def follow_dir(p, d):
    if d == 'N' :
        return Point(p.x, p.y-1)
    if d == 'E' :
        return Point(p.x+1, p.y)
    if d == 'S' :
        return Point(p.x, p.y+1)
    if d == 'W' :
        return Point(p.x-1, p.y)

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]


def part_1(lines):
    for y, line in enumerate(lines):
        try:
            start = Point(line.index('S'), y)
            break
        except ValueError:
            continue

    changed = True
    cnt = 0

    list_of_distances = []

    point = start
    starting_directions = []
    for fd in 'NESW':
        tn = follow_dir(start, fd)
        tc = lines[tn.y][tn.x] 

        if tc != '.' and tn.y >= 0 and tn.x >= 0:
            if fd == 'N' and tc in '|7F':
                starting_directions.append(fd)
            elif fd == 'S' and tc in '|LJ':
                starting_directions.append(fd)
            elif fd == 'E' and tc in '-LJ':
                starting_directions.append(fd)
            elif fd == 'W' and tc in '-FL':
                starting_directions.append(fd)

    for starting_direction in starting_directions:
        cur_char = None
        facing_direction = starting_direction

        # Take the first step
        point = follow_dir(start, starting_direction)

        distances = []
        cnt = 1
        while cur_char != 'S':
            cur_char = lines[point.y][point.x]

            if cur_char == '|':
                if facing_direction == 'N':
                    point.y -= 1
                elif facing_direction == 'S':
                    point.y += 1

                else:
                    raise Exception(f'WRONG | @ {point} [{lines[point.y][point.x]}] facing {facing_direction}')

            elif cur_char == '-':
                if facing_direction == 'E':
                    point.x += 1
                elif facing_direction == 'W':
                    point.x -= 1

                else:
                    raise Exception(f'WRONG - @ {point} [{lines[point.y][point.x]}] facing {facing_direction}')

            elif cur_char == 'L':
                if facing_direction == 'S':
                    facing_direction = 'E'
                    point.x += 1
                elif facing_direction == 'W':
                    facing_direction = 'N'
                    point.y -= 1

                else:
                    raise Exception(f'WRONG L @ {point} [{lines[point.y][point.x]}] facing {facing_direction}')

            elif cur_char == 'J':
                if facing_direction == 'E':
                    facing_direction = 'N'
                    point.y -= 1
                elif facing_direction == 'S':
                    facing_direction = 'W'
                    point.x -= 1

                else:
                    raise Exception(f'WRONG J @ {point} [{lines[point.y][point.x]}] facing {facing_direction}')

            elif cur_char == '7':
                if facing_direction == 'E':
                    facing_direction = 'S'
                    point.y += 1
                elif facing_direction == 'N':
                    facing_direction = 'W'
                    point.x -= 1

                else:
                    raise Exception(f'WRONG 7 @ {point} [{lines[point.y][point.x]}] facing {facing_direction}')

            elif cur_char == 'F':
                if facing_direction == 'N':
                    facing_direction = 'E'
                    point.x += 1
                elif facing_direction == 'W':
                    facing_direction = 'S'
                    point.y += 1

                else:
                    raise Exception(f'WRONG F @ {point} [{lines[point.y][point.x]}] facing {facing_direction}')

            elif cur_char == 'S':
                continue

            distances.append(cnt)

            cnt += 1

        list_of_distances.append(distances)

    first = list_of_distances.pop()
    second = list_of_distances.pop()

    for f, s in zip(first, second[::-1]):
        if f-s == 0:
            return f


test_lines = [
        '..F7.',
        '.FJ|.',
        'SJ.L7',
        '|F--J',
        'LJ...',
        ]
t = part_1(test_lines)
assert t == 8, t

print('Part 1: ', part_1(lines))

