from collections import Counter

with open('input.txt') as f:
    lines = f.readlines()

def part_1(lines):
    a = []
    b = []

    for line in lines:
        if not line.strip():
            continue

        A, B = line.split()

        a.append(A)
        b.append(B)

    a.sort()
    b.sort()

    diff = 0
    for x,y in zip(a, b):
        diff += abs(int(x)-int(y))

    return diff

print('part 1', part_1(lines))

def part_2(lines):
    a = []
    b = []

    for line in lines:
        if not line.strip():
            continue

        A, B = line.split()

        a.append(int(A))
        b.append(int(B))

    c = Counter(b)

    s = 0
    for item in a:
        if item in c:
            s += item * c[item]
    return s

print('part 2', part_2(lines))

