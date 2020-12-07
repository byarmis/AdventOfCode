import time
start = time.time()

with open('input.txt') as f:
    raw = f.readlines()

with open('tst.txt') as f:
    tst = f.readlines()


from collections import defaultdict

def get_rules(raw):
    rules = defaultdict(list)

    for line in raw:
        parent, children = line.split(' contain ')
        parent = ' '.join(parent.split(' ')[:2])

        if children.strip() == 'no other bags.':
            rules[parent] = [[]]
            continue

        parsed_children = []
        for child in children.split(','):
            c = child.replace('bags', '')
            c = c.replace('bag', '')
            c = c.replace('.','')
            c = c.strip()

            num = int(c[0])
            color = c[1:].strip()
            parsed_children.append([color, num])

        rules[parent] = parsed_children

    return rules

# Part one

def part_1(raw):
    rules = get_rules(raw)

    def can_contain_gold(color):
        if rules[color] == [[]]:
            return False

        if 'shiny gold' in {c[0] for c in rules[color]}:
            return True
        return any(can_contain_gold(c[0]) for c in rules[color])

    cnt = 0
    for color in rules:
        if can_contain_gold(color):
            cnt += 1

    return cnt

print('Part one:', part_1(raw))

def part_2(raw):
    rules = get_rules(raw)

    # Part two
    def get_containing_bags(color):
        if rules[color] == [[]]:
            return 0

        return sum(c[1] for c in rules[color]) + sum(get_containing_bags(c[0])*c[1] for c in rules[color])


    r = get_containing_bags('shiny gold')

    return r

assert part_2(tst) == 32, part_2(tst)
print('Part two: ',  part_2(raw))

print('total time: ', time.time() - start)
