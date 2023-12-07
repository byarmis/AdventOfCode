from collections import Counter
from functools import total_ordering

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]


class WinType:
    def __init__(self, s, _):
        self.string = s
        c = Counter(s)

        if c.most_common(1)[0][1] == 5:
            self.val = 0
        elif c.most_common(1)[0][1] == 4:
            self.val = 1
        elif c.most_common(2)[0][1] == 3 and c.most_common(2)[1][1] == 2:
            self.val = 2
        elif c.most_common(1)[0][1] == 3:
            self.val = 3
        elif c.most_common(2)[0][1] == 2 and c.most_common(2)[1][1] == 2:
            self.val = 4
        elif c.most_common(1)[0][1] == 2:
            self.val = 5
        elif c.most_common(1)[0][1] == 1:
            self.val = 6

@total_ordering
class Hand:
    def __init__(self, s, cards, win_type):
        self.string = s
        self.win_type = win_type(s, cards)
        self._cards = cards

    def __lt__(self, other):
        if self.win_type.val < other.win_type.val:
            return False
        elif self.win_type.val > other.win_type.val:
            return True
        for s_c, o_c in zip(self.string, other.string):
            if s_c != o_c:
                return self._cards.index(s_c) > self._cards.index(o_c)

    def __eq__(self, other):
        return self.string == other.string

def part_1(lines):
    cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    hands = []
    for line in lines:
        hand, bid = line.split()
        hands.append((Hand(hand, cards, WinType), int(bid)))

    hands.sort()

    winnings = 0
    for loc, val in enumerate(hands, start=1):
        winnings += val[1] * loc

    return winnings

test_lines = [
        '32T3K 765',
        'T55J5 684',
        'KK677 28',
        'KTJJT 220',
        'QQQJA 483',
        ]

t = part_1(test_lines)
assert t == 6440, t
w = part_1(lines)
assert w != 251569201, w
assert w != 249431299, w
assert w != 249873612, w
print('Part 1: ', w)


class WinType2:
    def __init__(self, s, cards):
        vals = []
        self.string = s

        for card in cards:
            temp_s = s.replace('J', card)
            c = Counter(temp_s)

            if c.most_common(1)[0][1] == 5:
                vals.append( 0)
            elif c.most_common(1)[0][1] == 4:
                vals.append( 1)
            elif c.most_common(2)[0][1] == 3 and c.most_common(2)[1][1] == 2:
                vals.append( 2)
            elif c.most_common(1)[0][1] == 3:
                vals.append( 3)
            elif c.most_common(2)[0][1] == 2 and c.most_common(2)[1][1] == 2:
                vals.append( 4)
            elif c.most_common(1)[0][1] == 2:
                vals.append( 5)
            elif c.most_common(1)[0][1] == 1:
                vals.append( 6)
        self.val = min(vals)

def part_2(lines):
    cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    hands = []
    for line in lines:
        hand, bid = line.split()
        hands.append((Hand(hand, cards, WinType2), int(bid)))

    hands.sort()

    winnings = 0
    for loc, val in enumerate(hands, start=1):
        winnings += val[1] * loc

    return winnings

t = part_2(test_lines)
assert t == 5905, t
w = part_2(lines)
print('Part 2: ', w)
