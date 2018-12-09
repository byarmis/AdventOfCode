import itertools
from collections import deque

class Game:
    def __init__(self, players):
        self.array = deque([0])
        self.val = 0
        self.idx = 0
        self.players = [0 for _ in range(players)]

    @property
    def turn(self):
        return self.val % len(self.players)

    def add(self):
        self.val += 1
        if self.val % 23 == 0:
            self.players[self.turn] += self.val
            self.array.rotate(7)
            self.players[self.turn] += self.array.popleft()

        else:
            self.array.rotate(-2)
            self.array.appendleft(self.val)

def part_1(players, rounds):
    g = Game(players=players)
    for _ in range(rounds):
        g.add()

    return max(g.players)

assert part_1(9, 25) == 32
assert part_1(10, 1618) == 8317
assert part_1(13, 7999) == 146373
assert part_1(17, 1104) == 2764
assert part_1(21, 6111) == 54718
assert part_1(30, 5807) == 37305

print(part_1(429, 70901*100))

