test_input = [
    "addx 15",
    "addx -11",
    "addx 6",
    "addx -3",
    "addx 5",
    "addx -1",
    "addx -8",
    "addx 13",
    "addx 4",
    "noop",
    "addx -1",
    "addx 5",
    "addx -1",
    "addx 5",
    "addx -1",
    "addx 5",
    "addx -1",
    "addx 5",
    "addx -1",
    "addx -35",
    "addx 1",
    "addx 24",
    "addx -19",
    "addx 1",
    "addx 16",
    "addx -11",
    "noop",
    "noop",
    "addx 21",
    "addx -15",
    "noop",
    "noop",
    "addx -3",
    "addx 9",
    "addx 1",
    "addx -3",
    "addx 8",
    "addx 1",
    "addx 5",
    "noop",
    "noop",
    "noop",
    "noop",
    "noop",
    "addx -36",
    "noop",
    "addx 1",
    "addx 7",
    "noop",
    "noop",
    "noop",
    "addx 2",
    "addx 6",
    "noop",
    "noop",
    "noop",
    "noop",
    "noop",
    "addx 1",
    "noop",
    "noop",
    "addx 7",
    "addx 1",
    "noop",
    "addx -13",
    "addx 13",
    "addx 7",
    "noop",
    "addx 1",
    "addx -33",
    "noop",
    "noop",
    "noop",
    "addx 2",
    "noop",
    "noop",
    "noop",
    "addx 8",
    "noop",
    "addx -1",
    "addx 2",
    "addx 1",
    "noop",
    "addx 17",
    "addx -9",
    "addx 1",
    "addx 1",
    "addx -3",
    "addx 11",
    "noop",
    "noop",
    "addx 1",
    "noop",
    "addx 1",
    "noop",
    "noop",
    "addx -13",
    "addx -19",
    "addx 1",
    "addx 3",
    "addx 26",
    "addx -30",
    "addx 12",
    "addx -1",
    "addx 3",
    "addx 1",
    "noop",
    "noop",
    "noop",
    "addx -9",
    "addx 18",
    "addx 1",
    "addx 2",
    "noop",
    "noop",
    "addx 9",
    "noop",
    "noop",
    "noop",
    "addx -1",
    "addx 2",
    "addx -37",
    "addx 1",
    "addx 3",
    "noop",
    "addx 15",
    "addx -21",
    "addx 22",
    "addx -6",
    "addx 1",
    "noop",
    "addx 2",
    "addx 1",
    "noop",
    "addx -10",
    "noop",
    "noop",
    "addx 20",
    "addx 1",
    "addx 2",
    "addx 2",
    "addx -6",
    "addx -11",
    "noop",
    "noop",
    "noop",
]

def part_1(lines):
    cycle = 1
    X = 1
    signals = []

    for line in lines:
        if line.strip() == 'noop':
            cycle += 1

        elif 'addx' in line:
            val = int(line.split()[1])

            cycle += 1
            if is_interesting(cycle):
                signals.append(X*cycle)

            cycle += 1
            X += val

        if is_interesting(cycle):
            signals.append(X*cycle)

    return sum(signals)

def is_interesting(cycle):
    return cycle in {20, 60, 100, 140, 180, 220}

def update_rows(rows, row, cycle, X):
    if len(row) == 40:
        rows.append(row)
        row = []

    if (cycle % 40) - 1 <= X + 1 <= (cycle % 40) + 1:
        row.append('#')
    else:
        row.append('.')

    return rows, row


def part_2(lines):
    cycle = 1
    X = 1
    rows = []
    row = []

    for line in lines:
        if line.strip() == 'noop':
            rows, row = update_rows(rows, row, cycle, X)
            cycle += 1

        elif 'addx' in line:
            val = int(line.split()[1])

            rows, row = update_rows(rows, row, cycle, X)
            cycle += 1

            rows, row = update_rows(rows, row, cycle, X)
            X += val
            cycle += 1

    rows.append(row)
    for row in rows:
        print(''.join(row))

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()

    assert part_1(test_input) == 13140

    print('Part 1: ', part_1(lines))

    print('PART 2 TEST')
    part_2(test_input)

    print('='*40)

    print('PART 2')
    part_2(lines)
        

