import re

with open('input.txt') as f:
    lines = [l.rstrip('\n') for l in f]
    lines = [[int(i) for i in re.findall(r'-?\d+', l)] for l in lines]

nums = lines[0]
all_meta = []

def read(i):
    children = nums[i]
    meta = nums[i + 1]
    i += 2
    for j in xrange(children):
        i = read(i)
    for j in xrange(meta):
        all_meta.append(nums[i + j])
    return i + meta

read(0)
print sum(all_meta)
