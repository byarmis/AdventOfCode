from collections import defaultdict

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_closest(points, p):
    m = None
    for point in points:
        if m is None or dist(point, p) < m:
            cnt = 1
            m = dist(point, p)
            i = point

        elif dist(point, p) == m:
            cnt += 1

    if cnt > 1:
        return None

    return i

def parse_file(array_in):
    points = []
    for point in array_in:
        s = point.strip().split(',')
        points.append((int(s[0]), int(s[1]))) 

    return points

def part_2(array_in, lim):
    points = parse_file(array_in)

    xmin = min(points, key=lambda x: x[0])[0]
    xmax = max(points, key=lambda x: x[0])[0]

    ymin = min(points, key=lambda x: x[1])[1]
    ymax = max(points, key=lambda x: x[1])[1]

    in_region = 0
    for x in range(xmin, xmax+1):
        for y in range(ymin, ymax+1):
            d = sum([dist(point, (x,y)) for point in points])
            if d < lim:
                in_region += 1

    return in_region

def part_1(array_in):
    points = parse_file(array_in)

    xmin = min(points, key=lambda x: x[0])[0]
    xmax = max(points, key=lambda x: x[0])[0]

    ymin = min(points, key=lambda x: x[1])[1]
    ymax = max(points, key=lambda x: x[1])[1]

    edges = set()
    filled = defaultdict(int)
    for x in range(xmin, xmax+1):
        for y in range(ymin, ymax+1):
            c = get_closest(points, (x,y))
            filled[(x,y)] = c 

            if (x in (xmin, xmax) or y in (ymin, ymax)) and c is not None:
                edges.add(c)

    closest = defaultdict(int)
    for v in filled.values():
        if v is not None and v not in edges:
            closest[v] += 1

    return max(closest.values())

test = ['1, 1',
        '1, 6',
        '8, 3',
        '3, 4',
        '5, 5',
        '8, 9']

#assert part_1(test) == 17
assert part_2(test, 32) == 16

#with open('input.txt') as f:
    #print(part_1(f.readlines()))

with open('input.txt') as f:
    print(part_2(f.readlines(), 10000))

