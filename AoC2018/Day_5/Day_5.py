
def part_1(polymer):
    quit = False

    i = 0
    while not quit:
        quit = True

        for i in range(i, len(polymer)-1):
            if ((polymer[i].islower() and polymer[i+1].isupper()) or (polymer[i].isupper() and polymer[i+1].islower())) and polymer[i].lower() == polymer[i+1].lower():
                quit = False
                break

        if not quit:
            polymer = polymer[:i] + polymer[i+2:]
            i = max([i-1, 0])

    return len(polymer)

import string
def part_2(polymer):
    reduction = dict()
    for letter in string.ascii_lowercase:
        print(letter.upper())
        reduced_polymer = polymer.replace(letter, '').replace(letter.upper(), '')

        reduction[letter] = part_1(reduced_polymer)

    return min(reduction.values())

print(part_1('dabAcCaCBAcCcaDA'))
print(part_2('dabAcCaCBAcCcaDA'))

with open('input.txt') as f:
    polymer = f.readlines()
    polymer = polymer[0].strip()

print(part_1(polymer))
print(part_2(polymer))


