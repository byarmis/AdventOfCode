with open('input.txt') as f:
    exps = f.readlines()

class Problem:
    def __init__(self, s):
        self.m = {
                '+': lambda a, b: a+b,
                '*': lambda a, b: a*b,
            }
        s = s.strip().replace(' ', '')
        parsed = []
        start = 0
        while start < len(s):
            val = s[start]

            if val == '(':
                # Parse and slice
                p = 1
                end = start+1
                while p:
                    end_val = s[end]

                    if end_val == ')':
                        p -= 1
                    elif end_val == '(':
                        p += 1

                    end += 1

                parsed.append(Problem(s[start+1:end-1]))
                start = end

            else:
                parsed.append(val)
                start += 1

        self.parsed = parsed

    def solve(self):
        op = None

        for v in self.parsed:
            if isinstance(v, Problem):
                prev = v.solve()
            elif v.isdigit():
                prev = int(v)
            elif v in self.m:
                op = self.m[v]
                continue

            if op is not None:
                i = op(i, prev)
                op = None

            else:
                i = prev
                
        return i

    def __repr__(self):
        return self.parsed.__repr__()

tests = {
        '1+2*3+4*5+6': 71,
        '1 + (2 * 3) + (4 * (5 + 6))': 51,
        '2 * 3 + (4 * 5)': 26,
        '5 + (8 * 3 + 9 + 3 * 4 * 3)': 437,
        '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))': 12240,
        '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2': 13632
        }

for s, v in tests.items():
    t = Problem(s).solve() 
    assert t == v, (s, t, v)

print('Part one:', sum(Problem(e).solve() for e in exps))

class Problem_2:
    def __init__(self, s):
        self.m = {
                '+': lambda a, b: a+b,
                '*': lambda a, b: a*b,
            }
        s = s.strip().replace(' ', '')

        parsed = []
        start = 0
        while start < len(s):
            val = s[start]

            if val == '(':
                # Parse and slice
                p = 1
                end = start+1
                while p:
                    end_val = s[end]

                    if end_val == ')':
                        p -= 1
                    elif end_val == '(':
                        p += 1

                    end += 1

                parsed.append(Problem_2(s[start+1:end-1]))
                start = end

            else:
                parsed.append(val)
                start += 1

        self.parsed = parsed
        self.solution = None

    def solve(self):
        if self.solution is not None:
            return self.solution

        op = None
        hasPlus = True

        while hasPlus:
            hasPlus = False
            loc = 0
            while loc < len(self.parsed):
                v = self.parsed[loc]

                if isinstance(v, Problem_2):
                    i = v.solve()
                elif isinstance(v, int):
                    i = v
                elif v.isdigit():
                    i = int(v)
                elif v in self.m:
                    if v == '+':
                        hasPlus = True
                    elif v == '*':
                        loc += 1
                        continue

                    op = self.m[v]
                    loc += 1
                    continue

                if op is not None:
                    prev = int(self.parsed[loc-2])
                    p = self.parsed
                    for _ in range(3):
                        del p[loc-2]

                    loc -= 2
                    p.insert(loc, op(i, prev))
                    self.parsed = p
                    prev = i
                    op = None

                else:
                    prev = i

                loc += 1

        op = None
        # Took care of addition, now do mult
        for v in self.parsed:
            if isinstance(v, Problem_2):
                i = v.solve()
            elif isinstance(v, int):
                i = v
            elif v.isdigit():
                i = int(v)
            elif v in self.m:
                op = self.m[v]
                continue

            if op is not None:
                prev = op(i, prev)
                op = None

            else:
                prev = i
               
        self.solution = prev
        return self.solution

    def __repr__(self):
        return '<P'+self.parsed.__repr__()+'P>'

    def __int__(self):
        if self.solution is not None:
            return int(self.solution)
        else:
            self.solve()
            return int(self.solution)

tests = {
        '1+2*3+4*5+6': 231,
        '1 + (2 * 3) + (4 * (5 + 6))': 51,
        '2 * 3 + (4 * 5)': 46,
        '5 + (8 * 3 + 9 + 3 * 4 * 3)': 1445,
        '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))': 669060,
        '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2': 23340
        }

for s, v in tests.items():
    t = Problem_2(s).solve() 
    assert t == v, (s, t, v)

print('Part two:', sum(Problem_2(e).solve() for e in exps))

