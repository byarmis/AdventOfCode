from collections import defaultdict, deque

def day_15(nums, lmt):
    seen = defaultdict(lambda: deque(maxlen=2))
    for loc, val in enumerate(nums):
        seen[val].append(loc)

    spoken = nums[:]
    turn = len(nums)
    while turn < lmt:
        prev_num = spoken[-1]

        if len(seen[prev_num]) < 1:
            if len(seen[prev_num]) == 0:
                val = 0
            elif max(seen[prev_num]) == turn - 1:
                val = 0
            else:
                val = max(seen[prev_num]) - min(seen[prev_num]) 

        else:
            val = max(seen[prev_num]) - min(seen[prev_num]) 

        idx = len(spoken) 

        spoken.append(val)
        seen[val].append(idx)
        turn += 1

    return spoken[-1]

p = day_15([0,3,6], 2020) 
assert p == 436, p

L = [14,3,1,0,9,5]
print('part 1: ', day_15(L, 2020))
print('part 2: ', day_15(L, 30000000))

