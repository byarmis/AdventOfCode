from math import lcm

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

class Node:
    def __init__(self, s):
        self.s = s
        name, children = s.split('=')
        children = children.replace('(','').replace(')','').strip().split(',')

        self.left_str = children[0].strip()
        self.right_str = children[1].strip()
        self.name = name.strip()

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name


dirs = lines.pop(0)
_ = lines.pop(0)

nodes = [Node(s) for s in lines]
nodes = {n.name:n for n in nodes}

ptr = 'AAA'
steps = 0
while ptr != 'ZZZ':
    for d in dirs:
        n = nodes[ptr]
        if d == 'L':
            ptr = n.left_str
        if d == 'R':
            ptr = n.right_str

        steps += 1

print('Part 1: ', steps)

ptrs = [n for n in nodes.keys() if n[-1] == 'A']
step_arr = []

for ptr in ptrs:
    steps = 0
    while ptr[-1] != 'Z':
        for d in dirs:
            n = nodes[ptr]
            if d == 'L':
                ptr = n.left_str
            if d == 'R':
                ptr = n.right_str

            steps += 1
            if ptr[-1] == 'Z':
                break

    step_arr.append(steps)

print('Part 2: ', lcm(*step_arr))

