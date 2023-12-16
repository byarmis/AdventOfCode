from collections import defaultdict

with open('input.txt') as f:
    line = f.readline().strip()

def hash_func(S):
    val = 0
    for s in S:
        val += ord(s)
        val *= 17
        val %= 256

    return val


def part_1(line):
    summary = 0
    for S in line.split(','):
        summary += hash_func(S)

    return summary

test_line = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'

assert part_1(test_line) == 1320

print('Part 1: ', part_1(line))

def part_2(line):
    boxes = defaultdict(list)

    for step in line.split(','):
        if step.endswith('-'):
            box_str = step[:-1]
        else:
            box_str = step.split('=')[0]

        box_idx = hash_func(box_str)

        if '=' in step:
            focal_length = int(step[-1])
            box = boxes[box_idx]

            if box_str in {b[0] for b in box}:
                box_replacement = box.copy()
                for loc, val in enumerate(box_replacement):
                    if val[0] == box_str:
                        idx = loc
                        break
                box_replacement[idx] = (box_str, focal_length)
                boxes[box_idx] = box_replacement

            else:
                boxes[box_idx].append((box_str, focal_length))

        elif step.endswith('-'):
            box = boxes[box_idx]
            if box_str in {b[0] for b in box}:
                boxes[box_idx] = [b for b in box if b[0] != box_str]

        else:
            raise Exception(f'Unknown operation: {op} ({step})')

    focusing_power = 0
    for box, lenses in boxes.items():
        if not lenses:
            continue

        for loc, lens in enumerate(lenses):
            focusing_power += (box + 1) * (loc+1) * (lens[1])

    return focusing_power
        

t = part_2(test_line)
assert t == 145, t

print('Part 2: ', part_2(line))

