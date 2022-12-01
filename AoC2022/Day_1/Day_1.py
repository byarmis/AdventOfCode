elves = []
with open('input.txt') as f:
    elf = []
    for line in f.readlines():
        if line.strip():
            elf.append(int(line))
        else:
            elves.append(sum(elf))
            elf = []

print('Part 1: ', max(elves))

elves.sort()

print('Part 2: ', sum(elves[-3:]))

