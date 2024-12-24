
with open('input.txt') as f:
    lines = f.readlines()

def get_data(lines):
    data = []
    for line in lines:
        if not line.strip():
            continue

        l = line.split()
        data.append(list(map(int, l)))
    return data

def is_safe(line):
    old_diff = 0
    new_diff = 0
    for a, b in zip(line, line[1:]):
        new_diff = a - b
        if not -3 <= new_diff <= 3:
            return False

        if new_diff == 0:
            return False
        elif new_diff > 0 and old_diff < 0:
            return False
        elif new_diff < 0 and old_diff > 0:
            return False

        old_diff = new_diff

    return True


def part_1(data):
    safe = 0
    for line in data:
        if is_safe(line):
            safe += 1
    return safe


example = [
        '7 6 4 2 1',
        '1 2 7 8 9',
        '9 7 6 2 1',
        '1 3 2 4 5',
        '8 6 4 4 1',
        '1 3 6 7 9',
        ]
example_data = get_data(example)
assert part_1(example_data) == 2, part_1(example_data)

data = get_data(lines)
assert part_1(data) < 294
print('part 1', part_1(data))

def part_2(data):
    safe = 0
    for line in data:
        if is_safe(line):
            safe += 1
            continue

        for i in range(len(line)):
            new_line = line[:]
            del new_line[i]

            if is_safe(new_line):
                print(new_line)
                safe += 1
                break
    return safe

assert part_2(example_data) == 4, part_2(example_data)

assert part_2(data) < 492
print('part 2', part_2(data))

