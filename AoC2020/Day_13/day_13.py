with open('input.txt') as f:
    goal, schedule = f.readlines()

schedule = [s for s in schedule.split(',')]

def part_1(goal, schedule):
    time = int(goal)
    schedule = [int(s) for s in schedule if s != 'x']

    while not any(time % b == 0 for b in schedule):
        time += 1

    return (time-int(goal)) * [b for b in schedule if time%b == 0][0]

print('part 1: ', part_1(goal, schedule))
# https://github.com/bsounak/Aoc2020/blob/main/day13.py
# https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Search_by_sieving

# For example, let's consider data = [17, x, 13, 19]
# Bus ids 17, 13, 19 have indexes 0, 2, 3 respectively. The indexes
# represent the offset of the departures

# We need to find the smallest T, such that
# T % 17 is 0, which is 17-0
# T % 13 is 11, which is 13-2
# T % 19 is 16, which is 19-3

# To express in terms of congruences
# https://en.wikipedia.org/wiki/Modular_arithmetic
# We need to solve for T such that
# T ≋ 0 (mod 17)
# T ≋ 11 (mod 13)
# T ≋ 16 (mod 19)


# TOO SLOW :(
def part_2(schedule):
    # https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Search_by_sieving
    pairs = [(int(b) - loc, int(b)) for loc, b in zip(range(len(schedule)), schedule) if b!='x']
    pairs[0] = 0, pairs[0][0]
    pairs.sort(reverse=True)

    t, step = pairs[0]
    for p in pairs[1:]:
        while t%p[1] != p[0]:
            t += step

        step *= p[1]

    return t

# https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def part_2(schedule):
    # https://rosettacode.org/wiki/Chinese_remainder_theorem
    pairs = [(int(b) - loc, int(b)) for loc, b in zip(range(len(schedule)), schedule) if b!='x']
    pairs[0] = 0, pairs[0][0]

    return chinese_remainder([p[1] for p in pairs], [p[0] for p in pairs])

assert part_2(['17','x','13','19']) == 3417
assert part_2(['7','13','x','x','59','x','31','19']) == 1068781
assert part_2(['67','7','59','61']) == 754018
assert part_2(['67','x','7','59','61']) == 779210
assert part_2(['67','7','x','59','61']) == 1261476
assert part_2(['1789','37','47','1889']) == 1202161486

print('part 2: ', part_2(schedule))

