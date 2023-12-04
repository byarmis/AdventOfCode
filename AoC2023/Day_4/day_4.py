from collections import defaultdict

with open('input.txt') as f:
    lines = f.readlines()

def part_1(lines):
    points = 0

    for line in lines:
        card_txt, numbers = line.split(':')
        winning_nums, my_nums = numbers.split('|')

        winning_nums = set(int(i) for i in winning_nums.split())
        my_nums = set(int(i) for i in my_nums.split())

        if my_nums & winning_nums:
            points += 2**(len(my_nums & winning_nums) - 1)

    print(points)


part_1(lines)

def part_2(lines):
    cards = dict()
    card_queue = []

    for line in lines:
        card_txt, numbers = line.split(':')
        card_num = int(card_txt.split()[1])

        winning_nums, my_nums = numbers.split('|')

        winning_nums = set(int(i) for i in winning_nums.split())
        my_nums = set(int(i) for i in my_nums.split())

        cards_won = len(my_nums & winning_nums)
        cards[card_num] = cards_won

        for i in range(1, cards_won+1):
            card_queue.append(card_num + i)

    copies = defaultdict(int)
    iters = 0
    while card_queue:
        c = card_queue.pop()
        copies[c] += 1
        iters += 1

        for i in range(1, cards[c]+1):
            card_queue.append(c + i)

        if iters % 1000 == 0:
            print(len(card_queue))

    return sum(copies.values()) + len(lines)

test_lines = [
        'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
        'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
        'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
        'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
        'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
        'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11',
        ]

result = part_2(test_lines)
assert result == 30, result

print('Part 2: ', part_2(lines))

