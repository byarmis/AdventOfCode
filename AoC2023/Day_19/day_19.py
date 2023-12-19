import operator
import itertools

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]


class Part:
    def __init__(self, s):
        s = s.replace("{", "").replace("}", "")

        for pair in s.split(","):
            key, val = pair.split("=")
            setattr(self, key, int(val))

    def score(self):
        return self.x + self.m + self.a + self.s


class Workflow:
    def __init__(self, s):
        name, s = s.split("{")
        self.name = name
        s = s.replace("}", "")
        self.rules = s.split(",")

    def run(self, part):
        for rule in self.rules:
            if len(rule) == 1:
                if rule == "A":
                    raise AcceptionException()
                elif rule == "R":
                    raise RejectionException()
                else:
                    raise Exception(f"Unknown rule: {rule}")

            elif "<" in rule:
                a, num = rule.split("<")
                op = operator.lt
            elif ">" in rule:
                a, num = rule.split(">")
                op = operator.gt
            else:
                return rule

            num, dest = num.split(":")

            if op(getattr(part, a), int(num)):
                if dest == "A":
                    raise AcceptionException()
                elif dest == "R":
                    raise RejectionException()
                else:
                    return dest


class AcceptOrReject(Exception):
    pass


class AcceptionException(AcceptOrReject):
    pass


class RejectionException(AcceptOrReject):
    pass


def part_1(lines):
    workflows = dict()
    parts = []

    use_workflows = True
    for line in lines:
        if not line.strip():
            use_workflows = False
            continue

        if use_workflows:
            w = Workflow(line)
            workflows[w.name] = w

        else:
            parts.append(Part(line))

    accepted = []
    for part in parts:
        try:
            w = workflows["in"]
            while True:
                next_w = w.run(part)
                w = workflows[next_w]
        except AcceptOrReject as e:
            if isinstance(e, AcceptionException):
                accepted.append(part)

    return sum(p.score() for p in accepted)


test_lines = [
    "px{a<2006:qkq,m>2090:A,rfg}",
    "pv{a>1716:R,A}",
    "lnx{m>1548:A,A}",
    "rfg{s<537:gd,x>2440:R,A}",
    "qs{s>3448:A,lnx}",
    "qkq{x<1416:A,crn}",
    "crn{x>2662:A,R}",
    "in{s<1351:px,qqz}",
    "qqz{s>2770:qs,m<1801:hdj,R}",
    "gd{a>3333:R,R}",
    "hdj{m>838:A,pv}",
    "",
    "{x=787,m=2655,a=1222,s=2876}",
    "{x=1679,m=44,a=2067,s=496}",
    "{x=2036,m=264,a=79,s=2244}",
    "{x=2461,m=1339,a=466,s=291}",
    "{x=2127,m=1623,a=2188,s=1013}",
]
t = part_1(test_lines)
assert t == 19114, t

print("Part 1: ", part_1(lines))


def part_2(lines):
    cnt = 0

    workflows = dict()
    for line in lines:
        if not line.strip():
            break

        w = Workflow(line)
        workflows[w.name] = w

    return cnt


t = part_2(test_lines)
assert t == 167409079868000, t
