import re

with open('input.txt') as f:
    pwds = f.readlines()

valid = 0
for pw in pwds:
    if not pw.strip():
        continue

    s = re.split(r'(\d.*)-(\d.*) (\w): (.*)', pw)
    _, minimum, maximum, target, p, _ = re.split(r'(\d.*)-(\d.*) (\w): (.*)', pw)

    c = 0
    for s in p.strip():
        if s == target:
            c += 1

    if int(minimum) <= c <= int(maximum):
        valid += 1

print('Part 1: ', valid)

def is_valid(a, b, p, target):
    a = int(a) - 1
    b = int(b) - 1

    if a >= len(p) or b >= len(p):
        return False

    elif p[a] == target and p[b] != target:
        return True
    elif p[b] == target and p[a] != target:
        return True
    return False


valid = 0
for pw in pwds:
    if not pw.strip():
        continue

    s = re.split(r'(\d.*)-(\d.*) (\w): (.*)', pw)
    _, a, b, target, p, _ = re.split(r'(\d.*)-(\d.*) (\w): (.*)', pw)

    if is_valid(a, b, p, target):
        valid += 1

print('Part 2: ', valid)

