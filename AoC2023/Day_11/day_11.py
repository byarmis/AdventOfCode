
with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

def part_1(lines, scaler=1):
    empty_rows = {loc for loc, val in enumerate(lines) if '#' not in val}

    empty_cols = set(range(len(lines[0])))
    for line in lines:
        for loc, val in enumerate(line):
            if loc not in empty_cols:
                continue
            if val != '.':
                empty_cols.remove(loc)

    galaxies = []
    for y, line in enumerate(lines):
        for x, val in enumerate(line):
            if val == '#':
                galaxies.append((x,y))

    distances = dict()
    for source_idx, source in enumerate(galaxies[:-1]):
        for target in galaxies[source_idx + 1:]:
            x_min = min(source[0], target[0])
            x_max = max(source[0], target[0])
            x_dist = x_max - x_min + len({ec for ec in empty_cols if x_min < ec < x_max}) * scaler

            y_min = min(source[1], target[1])
            y_max = max(source[1], target[1])
            y_dist = y_max - y_min + len({er for er in empty_rows if y_min < er < y_max}) * scaler

            distances[(source, target)] = x_dist + y_dist

    return sum(distances.values())

def part_2(lines):
    return part_1(lines, 1_000_000 - 1)

print('Part 1: ', part_1(lines))
print('Part 2: ', part_2(lines))

