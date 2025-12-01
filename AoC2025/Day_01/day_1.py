
def get_lines():
    with open('input.txt') as f:
        return f.readlines()

def part_1(lines):
    val = 50
    cnt = 0

    for line in lines:
        line = line.strip()
        direction_letter = line[0]
        direction = 1 if direction_letter == 'R' else -1
        amt = int(line[1:])

        val += direction * amt
        if val > 99:
            val -= 100

        val %= 100

        if val == 0:
            cnt += 1

    return cnt

def part_2(lines):
    val = 50
    cnt = 0

    for line in lines:
        line = line.strip()
        direction_letter = line[0]
        direction = 1 if direction_letter == 'R' else -1
        amt = int(line[1:])

        for _ in range(amt):
            val += direction 
            if val > 99:
                val -= 100

            val %= 100

            if val == 0:
                cnt += 1

    return cnt



tst = [
    'L68',
    'L30',
    'R48',
    'L5 ',
    'R60',
    'L55',
    'L1 ',
    'L99',
    'R14',
    'L82',
]

assert part_1(tst) == 3
assert part_2(tst) == 6

print('Part 1:', part_1(get_lines()))
print('Part 2:', part_2(get_lines()))
