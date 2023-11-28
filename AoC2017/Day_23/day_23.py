from typing import Optional

def part_1(registers, instructions, limit: Optional[int]=None):
    ptr = 0
    mul_cnt = 0
    ins_cnt = 0

    stop = False

    while not stop and 0 <= ptr < len(instructions):
        raw_ins = instructions[ptr]
        ins, x, y = raw_ins.split()
        ins_cnt += 1

        if limit:
            stop = ins_cnt > limit

        match ins:
            case 'set':
                if y in registers:
                    registers[x] = registers[y]
                elif x in registers:
                    registers[x] = int(y)
                else:
                    raise Exception(f'Unknown instruction: {raw_ins}')
                ptr += 1

            case 'sub':
                if y in registers:
                    registers[x] -= registers[y]
                elif x in registers:
                    registers[x] -= int(y)
                else:
                    raise Exception(f'Unknown instruction: {raw_ins}')
                ptr += 1

            case 'mul':
                mul_cnt += 1

                if y in registers:
                    registers[x] *= registers[y]
                elif x in registers:
                    registers[x] *= int(y)
                else:
                    raise Exception(f'Unknown instruction: {raw_ins}')
                ptr += 1

            case 'jnz':
                x = registers[x] if x in registers else int(x)

                if x != 0:
                    ptr += int(y)
                else:
                    ptr += 1

    return mul_cnt, registers


def part_2(registers, instructions):
    new_reg = part_1(registers, instructions, limit=100)[1]

    start = new_reg['b']
    end = new_reg['c']

    step = -int(instructions[-2].split()[-1])

    h = 0
    for x in range(start, end+1, step):
        for i in range(2, x):
            if x % i == 0:
                h += 1
                break

    return h

        
with open('input.txt') as f:
    instructions = f.readlines()

part_1_registers = {reg: 0 for reg in 'abcdefgh'}
print('Part 1: ', part_1(part_1_registers, instructions)[0])

part_2_registers = {reg: 0 for reg in 'abcdefgh'}
part_2_registers['a'] = 1
print('Part 2: ', part_2(part_2_registers, instructions))

