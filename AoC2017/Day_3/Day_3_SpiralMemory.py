#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools
from itertools import product

def part_1(i):
    def add_another_layer(d):
        previous_max = max(d[-1].keys()) # Where the previous layer left off
        previous_min = min(d[-1].keys()) # Where the previous layer started

        # Since layers are circular, immediately after the max is the min

        current = previous_max + 1 # Start at one after the previous maximum

        # Initialize the dictionary we're going to add.  
        # It's not a corner and it points to the previous maximum
        to_add = {current:(previous_max, False)} 

        current += 1

        # Add each side
        for _ in range(4):
            # Add until corner
            while not d[-1][previous_min][1]:
                to_add[current] = (previous_min, False)
                previous_min += 1
                current += 1

            # Add corner
            to_add[current] = (previous_min, False)
            current += 1
            to_add[current] = (previous_min, True)
            current += 1
            to_add[current] = (previous_min, False)
            current += 1

            previous_min += 1

        # Adding the last corner (and the three squares associated with it) adds an 
        # extra square that has to be removed
        del to_add[current-1]

        d.append(to_add)
        return d

    def steps(i):
        '''
        So the memory layers are stored in a list.  A layer in memory is a dictionary whose keys
        are the number and its values are a tuple-- the first value is the value in the previous
        layer that is after the current square and the second value is if the current value is 
        a corner.  
        
        If we're on a corner, we need to add two moves instead of one and we point to
        the corner on the previous layer.

        '''
        d = [{1:(None, False)},
             {2:(1, False),
              3:(1, True), 
              4:(1, False),
              5:(1, True),
              6:(1, False),
              7:(1, True),
              8:(1, False),
              9:(1, True)}]

        # The value we're looking for in our spiral, i, needs to be in a spiral we've generated
        if i > 1:
            while i not in d[-1]:
                d = add_another_layer(d)
        else:
            d.pop()

        # Traverse through d, outside in
        count = 0

        for layer in d[::-1]:
            count += 1
            i, corner = layer[i]

            if corner:
                # We need to go diagonally, so add another
                count += 1

            if i is None:
                # We're done, there is no next one
                # Center -> Center is no moves, so subtract one
                count -= 1

        return count

    tests = ((1, 0),
             (12, 3),
             (23, 2),
             (1024, 31))

    for test_in, test_out in tests:
        assert steps(test_in) == test_out, 'Steps for {} does not equal {} ({})'.format(test_in, test_out, steps(test_in))

    return steps(i)


class Point:
    def __init__(self, x, y=None):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return 'Point({x}, {y})'.format(x=self.x, y=self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

class part_2:
    def __init__(self):
        self.DIRECTIONS = tuple(Point(p[0], p[1]) for p in product([-1,0,1], repeat=2) if p != (0,0))
        self.points = {Point(0,0): 1}
        self.point_stack = [1]

    def neighbor_sum(self, p):
        to_add = 0
        for d in self.DIRECTIONS:
            try:
                to_add += self.points[p+d]
            except KeyError:
                continue
        return to_add
 
    def run(self, goal):
        r = 1
        
        while self.point_stack[-1] < goal:
            self.point_stack = []
            # Add right
            for y in range(-r+1, r+1):
                ns = self.neighbor_sum(Point(r, y))
                self.points[Point(r, y)] = ns
                self.point_stack.append(ns)

            # Add top, left to right, except the top corner
            for x in range(r, -r-1, -1):
                ns = self.neighbor_sum(Point(x, r))
                self.points[Point(x, r)] = ns
                self.point_stack.append(ns)

            # Add left, top to bottom
            for y in range(r, -r-1, -1):
                ns = self.neighbor_sum(Point(-r, y))
                self.points[Point(-r, y)] = ns
                self.point_stack.append(ns)

            # Add bottom
            for x in range(-r, r+1):
                ns = self.neighbor_sum(Point(x, -r))
                self.points[Point(x, -r)] = ns
                self.point_stack.append(ns)

            r += 1

        while self.point_stack[-1] > goal:
            # Pop from the stack until we go less than the value we're looking for
            ret_val = self.point_stack.pop()

        return ret_val

if __name__ == '__main__':
    p = 361527
    print(part_1(p))
    print(part_2().run(p))

