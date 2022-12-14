import math 

test_input = [
"Monkey 0:",
"Starting items: 79, 98",
"Operation: new = old * 19",
"Test: divisible by 23",
"If true: throw to monkey 2",
"If false: throw to monkey 3",
"",
"Monkey 1:",
"Starting items: 54, 65, 75, 74",
"Operation: new = old + 6",
"Test: divisible by 19",
"If true: throw to monkey 2",
"If false: throw to monkey 0",
"",
"Monkey 2:",
"Starting items: 79, 60, 97",
"Operation: new = old * old",
"Test: divisible by 13",
"If true: throw to monkey 1",
"If false: throw to monkey 3",
"",
"Monkey 3:",
"Starting items: 74",
"Operation: new = old + 3",
"Test: divisible by 17",
"If true: throw to monkey 0",
"If false: throw to monkey 1",
]

class Monkey:
    def __init__(self, name, items, operation, test, if_true, if_false):
        self.name = name
        self.items = items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false

        self.inspections = 0

    def __str__(self):
        return f"Monkey_{self.name}:\n\t{self.items}\n\t{self.operation}\n\t{self.test}\n\t\t{self.if_true}\n\t\t{self.if_false}\n"

    def __repr__(self):
        return self.__str__()

    def inspect(self, monkeys):
        self.items = [self.operation.op(item) // 3 for item in self.items]

        for item in self.items:
            self.inspections += 1

            if item % self.test == 0:
                monkeys[self.if_true].items.append(item)
            else:
                monkeys[self.if_false].items.append(item)

        self.items = []

    def inspect2(self, monkeys, big_mod):
        self.items = [self.operation.op(item) % big_mod for item in self.items]

        for item in self.items:
            self.inspections += 1

            if item % self.test == 0:
                monkeys[self.if_true].items.append(item)
            else:
                monkeys[self.if_false].items.append(item)

        self.items = []


class Operation:
    def __init__(self, line):
        if line.endswith('old * old'):
            self.op = lambda x: x*x
            self.str = 'square'
        elif '*' in line:
            multiplicand = int(line.split('*')[1])
            self.op = lambda x: x * multiplicand
            self.str = f'{multiplicand } * x'
        elif '+' in line:
            addend = int(line.split('+')[1])
            self.op = lambda x: x + addend
            self.str = f'{addend} + x'

    def __str__(self):
        return self.str
    def __repr__(self):
        return self.str


def part_1(lines):

    monkeys = {}
    stats = {}

    for L in lines:
        if not L.strip():
            new_monkey = Monkey(**stats)
            monkeys[new_monkey.name] = new_monkey
            stats = {}

        line = L.strip()

        if line.startswith('Monkey'):
            stats['name'] = int(line.split()[1][:-1])

        elif line.startswith('Starting items'):
            stats['items'] = [int(i) for i in line.split(':')[1].split(',')]

        elif line.startswith('Operation'):
            stats['operation'] = Operation(line)

        elif line.startswith('Test'):
            stats['test'] = int(line.split('by')[1])

        elif line.startswith('If true'):
            stats['if_true'] = int(line.split(' ')[-1])
        elif line.startswith('If false'):
            stats['if_false'] = int(line.split(' ')[-1])

    new_monkey = Monkey(**stats)
    monkeys[new_monkey.name] = new_monkey

    for i in range(20):
        for name, monkey in monkeys.items():
            monkey.inspect(monkeys)

    inspections = sorted([monkey.inspections for monkey in monkeys.values()])

    return inspections[-1] * inspections[-2]

def part_2(lines):

    monkeys = {}
    stats = {}

    for L in lines:
        if not L.strip():
            new_monkey = Monkey(**stats)
            monkeys[new_monkey.name] = new_monkey
            stats = {}

        line = L.strip()

        if line.startswith('Monkey'):
            stats['name'] = int(line.split()[1][:-1])

        elif line.startswith('Starting items'):
            stats['items'] = [int(i) for i in line.split(':')[1].split(',')]

        elif line.startswith('Operation'):
            stats['operation'] = Operation(line)

        elif line.startswith('Test'):
            stats['test'] = int(line.split('by')[1])

        elif line.startswith('If true'):
            stats['if_true'] = int(line.split(' ')[-1])
        elif line.startswith('If false'):
            stats['if_false'] = int(line.split(' ')[-1])

    new_monkey = Monkey(**stats)
    monkeys[new_monkey.name] = new_monkey

    big_mod = math.prod(monkey.test for monkey in monkeys.values())

    for i in range(10_000):
        for name, monkey in monkeys.items():
            monkey.inspect2(monkeys, big_mod)

    inspections = sorted([monkey.inspections for monkey in monkeys.values()])

    return inspections[-1] * inspections[-2]


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()

    assert part_1(test_input) == 10605
    print('Part 1: ', part_1(lines))

    assert part_2(test_input) == 2713310158, part_2(test_input)
    print('Part 2: ', part_2(lines))

