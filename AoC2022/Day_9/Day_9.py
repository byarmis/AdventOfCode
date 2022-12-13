import math

test_input_1 = [
    "R 4", 
    "U 4", 
    "L 3", 
    "D 1", 
    "R 4", 
    "D 1", 
    "L 5", 
    "R 2", 
]

test_input_2 = [
    "R 5", 
    "U 8", 
    "L 8", 
    "D 3", 
    "R 17", 
    "D 10", 
    "L 25", 
    "U 20", 
]

def sign(x):
    return math.copysign(1, x)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash(self.to_tuple())

    def __repr__(self):
        return '{%s, %s}' % (self.x, self.y)

    def to_tuple(self):
        return (self.x, self.y)


def part_1(lines):
    head = Point(0,0)
    tail = Point(0,0)
    visited = {Point(0,0), }

    for line in lines:
        if not line.strip():
            continue

        direction, amt = line.split()
        if direction == "R":
            attr = 'x'
            mult = 1
        elif direction == "L":
            attr = 'x'
            mult = -1
        elif direction == "U":
            attr = 'y'
            mult = 1
        elif direction == "D":
            attr = 'y'
            mult = -1

        for _ in range(int(amt)):
            setattr(head, attr, getattr(head, attr) + mult)

            if tail_needs_to_move(head, tail):
                if head.x == tail.x:
                    tail.y += sign(head.y-tail.y)

                elif head.y == tail.y:
                    tail.x += sign(head.x-tail.x)

                else:
                    tail.x += sign(head.x-tail.x)
                    tail.y += sign(head.y-tail.y)

                visited.add(tail.to_tuple())

    return len(visited)

def part_2(lines):
    points = [Point(0,0) for _ in range(10)]
    visited = {Point(0,0).to_tuple(), }

    for line in lines:
        if not line.strip():
            continue

        direction, amt = line.split()
        if direction == "R":
            attr = 'x'
            mult = 1
        elif direction == "L":
            attr = 'x'
            mult = -1
        elif direction == "U":
            attr = 'y'
            mult = 1
        elif direction == "D":
            attr = 'y'
            mult = -1

        for _ in range(int(amt)):
            setattr(points[0], attr, getattr(points[0], attr) + mult)

            loc = 1

            while loc < len(points):
                if tail_needs_to_move(points[loc-1], points[loc]):
                    if points[loc-1].x == points[loc].x:
                        points[loc].y += sign(points[loc-1].y-points[loc].y)

                    elif points[loc-1].y == points[loc].y:
                        points[loc].x += sign(points[loc-1].x-points[loc].x)

                    else:
                        points[loc].x += sign(points[loc-1].x-points[loc].x)
                        points[loc].y += sign(points[loc-1].y-points[loc].y)

                loc += 1

                visited.add(points[-1].to_tuple())

    return len(visited)


def tail_needs_to_move(head, tail):
    if abs(head.x - tail.x) > 1:
        return True

    if abs(head.y - tail.y) > 1:
        return True

    return False

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()

    assert part_1(test_input_1) == 13
    print('Part 1: ', part_1(lines))

    assert part_2(test_input_2) == 36
    print('Part 2: ', part_2(lines))

