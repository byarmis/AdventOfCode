from queue import PriorityQueue as PQ

test_input = [
        "Sabqponm",
        "abcryxxl",
        "accszExk",
        "acctuvwj",
        "abdefghi",
]

class Node:
    def __init__(self, val, x, y):
        self.x = x
        self.y = y

        self.neighbors = set()

        self.is_start = val == 'S'
        self.is_end = val == 'E'

        if self.is_start:
            self.val = ord('a')
        elif self.is_end:
            self.val = ord('z')
        else:
            self.val = ord(val)

    def add_neighbors(self, neighbors):
        for neighbor in neighbors:
            if neighbor is self:
                pass
            elif self.val + 1 < neighbor.val:
                pass
            else:
                self.neighbors.add(neighbor)

    def distance_to(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __lt__(self, other):
        return self.val < other.val


def get_nodes(lines):
    nodes = [[Node(letter, x, y) for x, letter in enumerate(line)] for y, line in enumerate(lines)]
    for y, node_line in enumerate(nodes):
        for x, node in enumerate(node_line):
            neighbors = []
            if x > 0:
                # Left
                neighbors.append(nodes[y][x-1])

            if y > 0:
                # Up
                neighbors.append(nodes[y-1][x])

            try:
                # Right
                neighbors.append(nodes[y][x+1])
            except IndexError:
                pass

            try:
                # Down
                neighbors.append(nodes[y+1][x])
            except IndexError:
                pass

            node.add_neighbors(neighbors)

    flat_nodes = [n for node_line in nodes for n in node_line]

    return flat_nodes


def part_1(lines):
    flat_nodes = get_nodes(lines)
    return _part_1(flat_nodes)

def _part_1(flat_nodes):
    # Thanks https://www.redblobgames.com/pathfinding/a-star/introduction.html#astar
    start = [node for node in flat_nodes if node.is_start][0]
    end = [node for node in flat_nodes if node.is_end][0]

    frontier = PQ()
    frontier.put((start.distance_to(end), start))

    came_from = {start: None}
    costs = {start: 0}

    while not frontier.empty():
        _, current = frontier.get()

        if current == end:
            break

        for next_node in current.neighbors:
            new_cost = costs[current] + 1

            if next_node not in came_from or new_cost < costs[next_node]:
                costs[next_node] = new_cost
                priority = new_cost + next_node.distance_to(end)
                frontier.put((priority, next_node))
                came_from[next_node] = current

    if end not in came_from:
        step_count = float('inf')
    else:
        step_count = 0
        current = end
        while current != start:
            current = came_from[current]
            step_count += 1

    return step_count

def generate_possibilies(orig_nodes):
    nodes = orig_nodes[:]

    for node in nodes:
        if node.is_start:
            node.is_start = False

    for i in range(len(nodes)):
        if nodes[i].val == ord('a'):
            node_copy = nodes[:]

            node_copy[i].is_start = True
            yield node_copy
            node_copy[i].is_start = False

def part_2(lines):
    flat_nodes = get_nodes(lines)
    fastest_goal = float('inf')
    for possibility in generate_possibilies(flat_nodes):
        speed = _part_1(possibility)

        if speed < fastest_goal:
            fastest_goal = speed

    return fastest_goal

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()

    assert part_1(test_input) == 31, part_1(test_input)
    print('Part 1: ', part_1(lines))

    assert part_2(test_input) == 29, part_2(test_input)
    print('Part 2: ', part_2(lines))


