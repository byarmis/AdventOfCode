import string

with open('input.txt') as f:
    raw_rules = f.readlines()

class Rule:
    def __init__(self, s):
        self.name, r =  rule.split(':')

        a, b = r.split('or')
        x,y = a.split('-')
        X,Y = b.split('-')

        self.first = (int(x), int(y))
        self.second = (int(X), int(Y))

    def is_valid(self, other):
        return (self.first[0] <= int(other) <= self.first[1]) or (self.second[0] <= int(other) <= self.second[1])

    def is_departure(self):
        return 'departure' in self.name.lower()

class Ticket:
    def __init__(self, s):
        self.vals = [int(i) for i in s.split(',')]

    def __getitem__(self, i):
        return self.vals[i]

    def __len__(self):
        return len(self.vals)

    def __str__(self):
        return str(self.vals)

    def __repr__(self):
        return self.__str__()


rules = []
for rule in raw_rules:
    if ':' in rule and 'your' not in rule and 'nearby' not in rule:
        rules.append(Rule(rule))


invalid = 0
skip = False
tickets = []
for line in raw_rules:
    if skip:
        my_tix = Ticket(line)
        skip = False
        continue
    if 'your' in line:
        skip = True
        continue
    if ':' in line:
        continue
    if not line.strip():
        continue

    ticket_valid = True
    for num in line.split(','):
        n = int(num.strip())

        valid = False
        for r in rules:
            valid |= r.is_valid(n)

        if not valid:
            ticket_valid = False
            invalid += n

    if ticket_valid:
        tickets.append(Ticket(line))

print('part 1', invalid)


possibilities = {i: set(range(len(my_tix))) for i in range(len(rules))}
# Key = rule index, value = possible ticket number index

for rule_idx in possibilities:
    rule = rules[rule_idx]
    for i in range(len(my_tix)):
        for ticket in tickets:
            if not rule.is_valid(ticket[i]):
                possibilities[rule_idx].discard(i)

# Prune possibilities
changed = True
while changed:
    changed = False
    for rule_idx, ticket_idx in possibilities.items():
        if isinstance(ticket_idx, set) and len(ticket_idx) == 1:
            possibilities[rule_idx] = ticket_idx.pop()

            for to_delete in possibilities:
                if isinstance(possibilities[to_delete], set):
                    possibilities[to_delete].discard(possibilities[rule_idx])

            changed = True

mult = 1
for loc, rule in enumerate(rules):
    if rule.is_departure():
        mult *= my_tix[possibilities[loc]]

print('part two', mult)


