
s = 0
with open('input.txt') as f:
    for line in f:
        s += int(line)

print(s)

with open('input.txt') as f:
    i = [int(line) for line in f]

s = 0
seen = set()
line_counter = 0
while s not in seen:
    seen.add(s)

    s += i[line_counter]
    line_counter += 1
    line_counter %= len(i)

print(s)

