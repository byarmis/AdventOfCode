import re

def addr(parsed, registers):
    registers[parsed[-1]] = registers[parsed[0]] + registers[parsed[1]]
    return registers

def addi(parsed, registers):
    registers[parsed[-1]] = parsed[1] + registers[parsed[0]]
    return registers

def mulr(parsed, registers):
    registers[parsed[-1]] = registers[parsed[0]] * registers[parsed[1]]
    return registers

def muli(parsed, registers):
    registers[parsed[-1]] = parsed[1] * registers[parsed[0]]
    return registers

def bani(parsed, registers):
    registers[parsed[-1]] = registers[parsed[0]] & parsed[1]
    return registers

def banr(parsed, registers):
    registers[parsed[-1]] = registers[parsed[0]] & registers[parsed[1]]
    return registers

def bori(parsed, registers):
    registers[parsed[-1]] = registers[parsed[0]] | parsed[1]
    return registers

def borr(parsed, registers):
    registers[parsed[-1]] = registers[parsed[0]] | registers[parsed[1]]
    return registers

def seti(parsed, registers):
    registers[parsed[-1]] = parsed[0]
    return registers

def setr(parsed, registers):
    registers[parsed[-1]] = registers[parsed[0]]
    return registers

def gtri(parsed, registers):
    registers[parsed[-1]] = int(registers[parsed[0]] > parsed[1])
    return registers

def gtir(parsed, registers):
    registers[parsed[-1]] = int(parsed[0] > registers[parsed[1]])
    return registers

def gtrr(parsed, registers):
    registers[parsed[-1]] = int(registers[parsed[0]] > registers[parsed[1]])
    return registers

def eqri(parsed, registers):
    registers[parsed[-1]] = int(registers[parsed[0]] == parsed[1])
    return registers

def eqir(parsed, registers):
    registers[parsed[-1]] = int(parsed[0] == registers[parsed[1]])
    return registers

def eqrr(parsed, registers):
    registers[parsed[-1]] = int(registers[parsed[0]] == registers[parsed[1]])
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

with open('input.txt') as f:
    ip_reg = int(re.search(r'(\d)', f.readline()).group(1))
    program = [re.findall(r'(\w*) (\d*) (\d*) (\d*)', l)[0] for l in f.readlines() if l.strip()]

def solve(ip_reg, program, init_val=0):
    registers = [init_val,0,0,0,0,0]

    while 0 <= registers[ip_reg] < len(program):
        to_do = program[registers[ip_reg]]
        func = to_do[0]
        args = tuple(map(int, to_do[1:]))

        functions[func](args, registers)
        registers[ip_reg] += 1

    registers[ip_reg] -= 1
    return registers[0]

assert solve(0, [('seti','5', '0', '1',),
                 ('seti','6', '0', '2',),
                 ('addi','0', '1', '0',),
                 ('addr','1', '2', '3',),
                 ('setr','1', '0', '0',),
                 ('seti','8', '0', '4',),
                 ('seti','9', '0', '5',),]) == 6

print(solve(ip_reg, program))
print(solve(ip_reg, program, 1))
