from collections import deque

with open('input.txt') as f:
    nums = [int(i) for i in f.readlines()]

with open('tst.txt') as f:
    tst = [int(i) for i in f.readlines()]

def part_1(nums, LIMIT=25):
    d = deque()

    for num in nums:
        # Is num valid?
        if len(d) == LIMIT:
            if not any(abs(i-num) in d for i in d):
                return num

        d.append(num)

        if len(d) > LIMIT:
            d.popleft()

assert part_1(tst, 5) == 127, part_1(tst, 5)
print('part one:', part_1(nums))

def part_2(nums, invalid_val):
    for start in range(0, len(nums)-3):
        for qty in range(2, len(nums)-start):
            s = nums[start:qty+start]
            if sum(s) == invalid_val:
                return min(s) + max(s)

assert part_2(tst, part_1(tst, 5)) == 62,part_2(tst, part_1(tst, 5)) 

print('part two:', part_2(nums, part_1(nums)))

