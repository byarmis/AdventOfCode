import re

test_input = [
"[ ] [D] [ ]", 
"[N] [C] [ ]", 
"[Z] [M] [P]", 
" 1   2   3 ", 
"", 
"move 1 from 2 to 1", 
"move 3 from 1 to 3", 
"move 2 from 2 to 1", 
"move 1 from 1 to 2", 
]


def part_1(lines):
    header = []
    for line in lines:
        if not line.strip():
            break
        header.append(line)

    num_crates = max(int(i) for i in header[-1].split())

    crates = [[] for _ in range(num_crates)]


    for line in header[-2::-1]:
        matches = re.findall('\[(.)\]', line)

        for loc, match in enumerate(matches):
            if not match.strip():
                continue

            crates[loc].append(match)

    moves = [line.strip() for line in lines if line.startswith('move')]

    for move in moves:
        amt, src, dest = [int(i) for i in move.split(' ') if i.isdigit()]
        for _ in range(amt):
            c = crates[src-1].pop()
            crates[dest-1].append(c)

    return ''.join(c[-1] for c in crates)

def part_2(lines):
    header = []
    for line in lines:
        if not line.strip():
            break
        header.append(line)

    num_crates = max(int(i) for i in header[-1].split())

    crates = [[] for _ in range(num_crates)]


    for line in header[-2::-1]:
        matches = re.findall('\[(.)\]', line)

        for loc, match in enumerate(matches):
            if not match.strip():
                continue

            crates[loc].append(match)

    moves = [line.strip() for line in lines if line.startswith('move')]


    for move in moves:
        amt, src, dest = [int(i) for i in move.split(' ') if i.isdigit()]

        c = crates[src-1][-amt:]
        crates[dest-1].extend(c)
        crates[src-1] = crates[src-1][:-amt]

    return ''.join(c[-1] for c in crates)

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()

    assert part_1(test_input) == "CMZ"
    print('Part 1: ', part_1(lines))

    assert part_2(test_input) == "MCD"
    print('Part 2: ', part_2(lines))

