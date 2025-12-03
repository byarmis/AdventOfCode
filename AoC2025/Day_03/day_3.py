from functools import lru_cache

def max_row(r: str) -> int:
    max_val = 0
    max_loc = None
    for loc, val in enumerate(r[:-1]):
        if int(val) > max_val:
            max_val = int(val)
            max_loc = loc

    second_highest = 0
    second_highest_loc = None
    for loc, val in enumerate(r[max_loc+1:], start=max_loc+1):
        if int(val) > second_highest:
            second_highest = int(val)
            second_highest_loc = loc

    return max_val*10 + second_highest


def part_1(lines: list[str]) -> int:
    return sum(max_row(r.strip()) for r in lines)

tst = [
    '987654321111111',
    '811111111111119',
    '234234234234278',
    '818181911112111',
]

assert max_row(tst[0]) == 98
assert max_row(tst[1]) == 89
assert max_row(tst[2]) == 78
assert max_row(tst[3]) == 92

assert part_1(tst) == 357

with open('input.txt') as f:
    lines = f.readlines()

print('Part 1: ', part_1(lines))

def max_twelve(r: str) -> int:

    @lru_cache
    def recurse(i, left):
        if left < 0:
            return 0

        if i >= len(r):
            # If we fall off the end, don't include zeros
            return -float('inf')

        return max(
                recurse(i+1, left)                          # Skip current number
                , 10**left*int(r[i]) + recurse(i+1, left-1) # Include current number
                )

    return recurse(0, 11)

def part_2(lines: list[str]) -> int:
    return sum(max_twelve(r.strip()) for r in lines)

assert max_twelve(tst[0]) == 987654321111
assert max_twelve(tst[1]) == 811111111119
assert max_twelve(tst[2]) == 434234234278
assert max_twelve(tst[3]) == 888911112111

assert part_2(tst) == 3121910778619

print('Part 2: ', part_2(lines))
