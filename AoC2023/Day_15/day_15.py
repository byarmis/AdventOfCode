
with open('input.txt') as f:
    line = f.readline().strip()

def part_1(line):
    summary = 0
    for S in line.split(','):
        val = 0
        for s in S:
            val += ord(s)
            val *= 17
            val %= 256

        summary += val
    return summary

test_line = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'

assert part_1(test_line) == 1320

print('Part 1: ', part_1(line))


