import itertools

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def copy(self):
        return Point(self.x, self.y)

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

    cnt = 0
    point = start

    for fd in 'NESW':
        tn = follow_dir(start, fd)
        tc = lines[tn.y][tn.x] 

        if tc != '.' and tn.y >= 0 and tn.x >= 0:
            if fd == 'N' and tc in '|7F':
                facing_direction = fd
            elif fd == 'S' and tc in '|LJ':
                facing_direction = fd
            elif fd == 'E' and tc in '-LJ':
                facing_direction = fd
            elif fd == 'W' and tc in '-FL':
                facing_direction = fd

    cur_char = None

    # Take the first step
    start_direction = facing_direction
    point = follow_dir(start, facing_direction)
    pipe_points = {start.copy(), point.copy()}

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

        else:
            raise Exception(f"What's that?! {cur_char}")

        pipe_points.add(point.copy())
        cnt += 1

    if start_direction == 'N' and facing_direction == 'N':
        start_replacement = '|'
    elif start_direction == 'N' and facing_direction == 'E':
        start_replacement = 'J'
    elif start_direction == 'N' and facing_direction == 'S':
        raise Exception('Should not happen 1')
    elif start_direction == 'N' and facing_direction == 'W':
        start_replacement = 'L'

    elif start_direction == 'E' and facing_direction == 'N':
        start_replacement = '7'
    elif start_direction == 'E' and facing_direction == 'E':
        start_replacement = '-'
    elif start_direction == 'E' and facing_direction == 'S':
        start_replacement = 'J'
    elif start_direction == 'E' and facing_direction == 'W':
        raise Exception('Should not happen 2')

    elif start_direction == 'S' and facing_direction == 'N':
        raise Exception('Should not happen 3')
    elif start_direction == 'S' and facing_direction == 'E':
        start_replacement = '7'
    elif start_direction == 'S' and facing_direction == 'S':
        start_replacement = '|'
    elif start_direction == 'S' and facing_direction == 'W':
        start_replacement = 'F'

    elif start_direction == 'W' and facing_direction == 'N':
        start_replacement = 'F'
    elif start_direction == 'W' and facing_direction == 'E':
        raise Exception('Should not happen 4')
    elif start_direction == 'W' and facing_direction == 'S':
        start_replacement = 'J'
    elif start_direction == 'W' and facing_direction == 'W':
        start_replacement = '-'


    return cnt // 2, pipe_points, start_replacement


test_lines = [
        '..F7.',
        '.FJ|.',
        'SJ.L7',
        '|F--J',
        'LJ...',
        ]
t = part_1(test_lines)[0]
assert t == 8, t

print('Part 1: ', part_1(lines)[0])

def part_2(lines):
    VERTICAL_CHARS = set('|LJ')

    _, pipe, start_replacement = part_1(lines)
    inside_cnt = 0

    for y, line in enumerate(lines):
        pipes_crossed = 0
        line = line.replace('S', start_replacement)

        for x, char in enumerate(line):
            if Point(x, y) in pipe and char in VERTICAL_CHARS:
                pipes_crossed += 1

            elif Point(x, y) not in pipe:
                inside_cnt += pipes_crossed % 2

    return inside_cnt

test_arr = [
        [['...........',
          '.S-------7.', 
          '.|F-----7|.', 
          '.||.....||.', 
          '.||.....||.', 
          '.|L-7.F-J|.', 
          '.|..|.|..|.', 
          '.L--J.L--J.', 
          '...........', 
        ], 4],

        [['.F----7F7F7F7F-7....',
          '.|F--7||||||||FJ....',
          '.||.FJ||||||||L7....',
          'FJL7L7LJLJ||LJ.L-7..',
          'L--J.L7...LJS7F-7L7.',
          '....F-J..F7FJ|L7L7L7',
          '....L7.F7||L7|.L7L7|',
          '.....|FJLJ|FJ|F7|.LJ',
          '....FJL-7.||.||||...',
          '....L---J.LJ.LJLJ...',
        ], 8],

        [['FF7FSF7F7F7F7F7F---7',
          'L|LJ||||||||||||F--J',
          'FL-7LJLJ||||||LJL-77',
          'F--JF--7||LJLJ7F7FJ-',
          'L---JF-JLJ.||-FJLJJ7',
          '|F|F-JF---7F7-L7L|7|',
          '|FFJF7L7F-JF7|JL---7',
          '7-L-JL7||F7|L7F-7F7|',
          'L.L7LFJ|||||FJL7||LJ',
          'L7JLJL-JLJLJL--JLJ.L',
        ], 10],

        [['...........',
          '...........', 
          '...........', 
          '....F---7F.', 
          '....|.F-S|.', 
          '....|.L-7|.', 
          '....|...|..', 
          '....L---J..', 
          '...........', 
        ], 5],
        ]
for test_lines, expected_val in test_arr:
    t = part_2(test_lines)
    assert t == expected_val, f'Return val: {t}, expected val: {expected_val}'

assert part_2(lines) < 475
print('Part 2: ', part_2(lines))

