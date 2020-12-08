with open('input.txt') as f:
    instructions = f.readlines()

def comp(instructions):
    acc = 0
    ran = set()
    ptr = 0

    while ptr not in ran and ptr < len(instructions):
        ins, amt = instructions[ptr].split(' ')

        ran.add(ptr)
        if ins == 'nop':
            ptr += 1
        elif ins == 'acc':
            acc += int(amt)
            ptr += 1
        elif ins == 'jmp':
            ptr += int(amt)

    return acc, ptr == len(instructions)

print('part one', comp(instructions)[0])

def possible_instructions(instructions):
    new = instructions[:]

    for loc, val in enumerate(instructions):
        if val.startswith('jmp'):
            new[loc] = 'nop 0'
        elif val.startswith('nop'):
            new[loc] = val.replace('nop', 'jmp')

        yield new

        new = instructions[:]

for instructions in possible_instructions(instructions):
    c = comp(instructions)
    if c[1]:
        print('part two', c[0])
        break


