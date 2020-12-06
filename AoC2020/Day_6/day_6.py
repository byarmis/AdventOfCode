with open('input.txt') as f:
    raw = f.readlines()

def parser(raw):
    groups = []
    tentative = []
    for line in raw:
        if not line.strip():
            groups.append(tentative)
            tentative = []
        else:
            tentative.append(line.strip())
    groups.append(tentative)

    return groups


def part_1(raw):
    groups = parser(raw)

    yes_cnt = 0
    for group in groups:
        group_yes = set()
        for person in group:
            group_yes |= set(person)

        yes_cnt += len(group_yes)

    return yes_cnt

with open('test.txt') as f:
    tst = f.readlines()


assert part_1(tst) == 11, part_1(tst)
print('Part 1: ', part_1(raw))


def part_2(raw):
    groups = parser(raw)
    yes_cnt = 0
    for group in groups:
        group_yes = set(group[0])
        for person in group:
            group_yes &= set(person)

        yes_cnt += len(group_yes)

    return yes_cnt

assert part_2(tst) == 6, part_2(tst)
print('Part 2: ', part_2(raw))

