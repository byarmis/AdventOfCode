import collections
twos =0
threes=0
with open('input.txt') as f:
    for line in f:
        c = collections.Counter()
        for letter in line.strip():
            c[letter] +=1

        found_two=False
        found_three=False
        for k in c:
            if not found_two and c[k] == 2:
                twos +=1
                found_two=True
            elif not found_three and c[k] ==3:
                threes +=1
                found_three=True
print(twos*threes)

import itertools

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

perms = []
current_max = len(lines[0])
for perm in itertools.permutations(lines, 2):
    diff = 0
    for letter_pair in zip(*perm):
        if letter_pair[0] != letter_pair[1]:
            diff += 1
    if diff < current_max:
        current_max = diff
        perms.append(perm)

for letter in zip(*perms[-1]):
    if letter[0] == letter[1]:
        print(letter[0], end='')

print(perms[-1])
