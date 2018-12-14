
def part_1(scores, puzzle_input):

    def get_next(scores, e1, e2):
        e1 += scores[e1] + 1
        e1 %= len(scores)

        e2 += scores[e2]  + 1
        e2 %= len(scores)

        new_val = scores[e1] + scores[e2]
        scores.extend(list(int(i) for i in str(new_val)))

        return e1, e2

    e1 = 0
    e2 = 1
    while len(scores) < puzzle_input + 11:
        e1, e2 = get_next(scores, e1, e2)

    return int(''.join(map(str, scores[puzzle_input:puzzle_input+10])))

def part_2(scores, puzzle_input):

    def get_next(scores, e1, e2):
        e1 += scores[e1] + 1
        e1 %= len(scores)

        e2 += scores[e2]  + 1
        e2 %= len(scores)

        new_val = scores[e1] + scores[e2]
        scores.extend(list(map(int, str(new_val))))

        return e1, e2

    e1 = 0
    e2 = 1

    pi = list(map(int, str(puzzle_input)))

    while pi != scores[-len(pi):] and pi!=scores[-len(pi)-1:-1]:
        e1, e2 = get_next(scores, e1, e2)

    if pi == scores[-len(pi):]:
        return len(scores) - len(pi)
    else:
        return len(scores) - len(pi) -1

scores= [3, 7]

assert part_1(scores[:], 9) == 5158916779, part_1(scores[:], 9)

puzzle_input = 825401
print('Part 1:', part_1(scores[:], puzzle_input))

assert part_2(scores[:], '51589') == 9, part_2(scores[:], '51589')
assert part_2(scores[:], '01245') == 5
assert part_2(scores[:], '92510') == 18, part_2(scores[:], '92510') 
assert part_2(scores[:], '59414') == 2018 
print('Test cases pass')

print('Part 2:', part_2(scores[:], str(puzzle_input)))

