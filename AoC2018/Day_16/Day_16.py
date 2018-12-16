import re

def addr(parsed, registers):
    registers[parsed[-1]] = registers[parsed[1]] + registers[parsed[2]]
    return registers

def addi(parsed, registers):
    registers[parsed[-1]] = parsed[2] + registers[parsed[1]]
    return registers

def mulr(parsed, registers):
    registers[parsed[-1]] = registers[parsed[1]] * registers[parsed[2]]
    return registers

def muli(parsed, registers):
    registers[parsed[-1]] = parsed[2] * registers[parsed[1]]
    return registers

def bani(parsed, registers):
    registers[parsed[-1]] = registers[parsed[1]] & parsed[2]
    return registers

def banr(parsed, registers):
    registers[parsed[-1]] = registers[parsed[1]] & registers[parsed[2]]
    return registers

def bori(parsed, registers):
    registers[parsed[-1]] = registers[parsed[1]] | parsed[2]
    return registers

def borr(parsed, registers):
    registers[parsed[-1]] = registers[parsed[1]] | registers[parsed[2]]
    return registers

def seti(parsed, registers):
    registers[parsed[-1]] = parsed[1]
    return registers

def setr(parsed, registers):
    registers[parsed[-1]] = registers[parsed[1]]
    return registers

def gtri(parsed, registers):
    registers[parsed[-1]] = int(registers[parsed[1]] > parsed[2])
    return registers

def gtir(parsed, registers):
    registers[parsed[-1]] = int(parsed[1] > registers[parsed[2]])
    return registers

def gtrr(parsed, registers):
    registers[parsed[-1]] = int(registers[parsed[1]] > registers[parsed[2]])
    return registers

def eqri(parsed, registers):
    registers[parsed[-1]] = int(registers[parsed[1]] == parsed[2])
    return registers

def eqir(parsed, registers):
    registers[parsed[-1]] = int(parsed[1] == registers[parsed[2]])
    return registers

def eqrr(parsed, registers):
    registers[parsed[-1]] = int(registers[parsed[1]] == registers[parsed[2]])
    return registers

functions = {
        'addr':addr,
        'addi':addi,

        'mulr':mulr,
        'muli':muli,

        'banr':banr,
        'bani':bani,

        'borr':borr,
        'bori':bori,

        'setr':setr,
        'seti':seti,

        'gtir':gtir,
        'gtri':gtri,
        'gtrr':gtrr,

        'eqir':eqir,
        'eqri':eqri,
        'eqrr':eqrr
}


def part_1(test=False):
    before = []
    code = []
    after = []
    with open('input.txt') as f:
        while True:
            b = f.readline()
            if 'Before' not in b:
                break

            before.append([int(i) for i in re.findall(r'\d', b)])
            code.append([int(i) for i in f.readline().split(' ')])
            after.append([int(i) for i in re.findall(r'\d', f.readline())])
            _ = f.readline()

    if test:
        before = ([3,2,1,1],)
        code = ([9,2,1,2],)
        after = ([3,2,2,1],)

    names_not_num = {name:set() for name in functions}

    three_plus_count = 0
    for sample in zip(before, code, after):
        sample_count = 0 
        for name, fun in functions.items():
            if fun(sample[1], sample[0][:]) == sample[2]:
                sample_count += 1
            else:
                names_not_num[name].add(sample[1][0])

        if sample_count >= 3:
            three_plus_count += 1

    if test:
        assert sample_count == 3
        assert three_plus_count == 1

    names_num = dict()
    for name in functions:
        names_num[name] = set(range(16)) - names_not_num[name]

    taken = set()
    while sum(isinstance(v, set) for v in names_num.values()) > 0:
        # If there are any that can be only 1, set it to that item
        for k, v in names_num.items():
            if isinstance(v, int):
                continue

            if len(v) == 1:
                names_num[k] = list(v)[0]
                taken.add(names_num[k])

        for k, v in names_num.items():
            if not isinstance(v, set):
                continue
            names_num[k] = v-taken

    return three_plus_count, names_num

p1 = part_1()
print(p1[0])

def part_2(names_num):
    num_names = {v:k for k, v in names_num.items()}

    with open('input.txt') as f:

        while True:
            l = f.readline()
            if 'Before' in l:
                _ = f.readline()
                _ = f.readline()
                _ = f.readline()

            else:
                break
        raw_program = f.readlines()

    program = []
    for line in raw_program:
        if not line.strip():
            continue

        program.append(list(map(int, line.split())))

    registers = [0,0,0,0]
    for line in program:
        functions[num_names[line[0]]](line, registers)
    
    return registers[0]

print(part_2(p1[1]))

