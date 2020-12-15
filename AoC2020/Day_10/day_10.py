with open('input.txt') as f:
    adapters = [int(i) for i in f.readlines()]

with open('tst.txt') as f:
    tst = [int(i) for i in f.readlines()]

def part_1(adapters):
    adapters = sorted(adapters)
    one_diff = 1
    three_diff = 0

    for a1, a2 in zip(adapters, adapters[1:]):
        if a2 - a1 == 3:
            three_diff += 1
        elif a2 - a1 == 1:
            one_diff += 1

    three_diff += 1

    return one_diff * three_diff

assert part_1(tst) == 220, part_1(tst)

print('part one:', part_1(adapters))

def part_2(adapters):
    adapters = sorted(adapters)
    adapters.append(adapters[-1]+3)
    adapters = [0] + adapters

    c = [0] * len(adapters)
    c[0] = 1

    for i in range(1, len(adapters)):
        for j in range(4):
            try:
                if adapters[i] - adapters[i-j] <= 3:
                    c[i] += c[i-j]
            except IndexError:
                pass

    return c[-1]

assert part_2(tst) == 19208
print('part two:', part_2(adapters))

