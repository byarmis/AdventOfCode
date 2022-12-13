import string

test_input = [
    "vJrwpWtwJgWrhcsFMMfFFhFp", 
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", 
    "PmmdzqPrVvPwwTWBwg", 
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", 
    "ttgJtRGJQctTZtZT", 
    "CrZsJsPPZsGzwwsLwLmpwMDw", 
]

PRIORITIES = ' '+ string.ascii_lowercase + string.ascii_uppercase


def part_1(lines):
    p = 0

    for line in lines:
        first, second = line[:len(line)//2], line[len(line)//2:]
        common = set(first) & set(second)
        e, *_ = common

        p += PRIORITIES.index(e)

    return p

def part_2(lines):
    p = 0
    while lines:
        first = lines.pop().strip()
        second = lines.pop().strip()
        third = lines.pop().strip()


        common = set(first) & set(second) & set(third)
        e, *_ = common

        p += PRIORITIES.index(e)

    return p

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()

    assert part_1(test_input) == 157

    print('Part 1: ', part_1(lines))

    assert part_2(test_input) == 70

    print('Part 2: ', part_2(lines))


