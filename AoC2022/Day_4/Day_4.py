
test_input = [
    "2-4,6-8", 
    "2-3,4-5", 
    "5-7,7-9", 
    "2-8,3-7", 
    "6-6,4-6", 
    "2-6,4-8", 
]

def part_1(lines):
    overlap = 0
    for line in lines:
        if not line.strip():
            continue

        first, second = line.strip().split(',')

        first_min, first_max = first.split('-')
        second_min, second_max = second.split('-')

        if int(first_min) <= int(second_min) and int(first_max) >= int(second_max):
            overlap += 1
        elif int(second_min) <= int(first_min) and int(second_max) >= int(first_max):
            overlap += 1

    return overlap

def part_2(lines):
    overlap = 0
    for line in lines:
        if not line.strip():
            continue

        first, second = line.strip().split(',')

        first_min, first_max = [int(i) for i in first.split('-')]
        second_min, second_max = [int(i) for i in second.split('-')]

        if first_max >= second_min and first_min <= second_max:
            overlap += 1

    return overlap


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()

    assert part_1(test_input) == 2

    print('Part 1: ', part_1(lines))

    assert part_2(test_input) == 4, part_2(test_input)

    print('Part 2: ', part_2(lines))

