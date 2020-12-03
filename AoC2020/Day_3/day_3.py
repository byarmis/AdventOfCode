with open('input.txt') as f:
    graph = f.readlines()

tree_count = 0
x = 0
for line in graph:
    if line[x] == '#':
        tree_count += 1
    x += 3
    x %= len(line.strip())

print('Part one: ', tree_count)

slopes = (1, 3, 5, 7)
mult_count = 1
for slope in slopes:
    tree_count = 0
    x = 0
    for line in graph:
        if line[x] == '#':
            tree_count += 1
        x += slope
        x %= len(line.strip())

    mult_count *= tree_count

tree_count = 0
x = 0
for line in graph[::2]:
    if line[x] == '#':
        tree_count += 1
    x += 1
    x %= len(line.strip())

mult_count *= tree_count

print('Part two: ', mult_count)

