def part_1(mass):
    m = int(mass)
    return (m // 3) - 2

def part_2(mass):
    m = int(mass)
    r = (m // 3) - 2
    if r < 0:
        return 0
    return r + part_2(r)


s1 = 0
with open('input.txt') as f:
    for line in f.readlines():
        s1 += part_1(line.strip())
print(f'part 1: {s1}')

s2 = 0
with open('input.txt') as f:
    for line in f.readlines():
        s2 += part_2(line)
print(f'part 2: {s2}')


