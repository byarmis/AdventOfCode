#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools

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

        # Traverse through d, outside in
        count = 0
        for layer in d[::-1]:
            if i in layer:
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

    print(steps(i))



def part_2(i):
    def allocate_next_ring(m):
        '''
        Takes a matrix, returns the same data, but with a ring of None-s added 
        around the existing data.

        Size of the matrix returned has two additional rows and each row is two 
        longer than original.
        '''

        new_m = [[None for _ in range(len(m)+2)]]
        for row in m:
            new_m.append([None] + row + [None])
        new_m.append([None for _ in range(len(m)+2)])

        return new_m

    def add_ring(m):
        m = allocate_next_ring(m)

        # Second from bottom right
        m[-2][-1] = m[-2][-2] + m[-3][-2]

        # Go up the right side
        row = -3
        while row > -len(m[0]) + 1:
            new_val = m[row][-2]    # Next to it 
            new_val += m[row-1][-2] # Diagonal up
            new_val += m[row+1][-2] # Diagonal down

            new_val += m[row+1][-1] # Below it

            m[row][-1] = new_val

            row -= 1

        # Second from top right
        m[1][-1] = m[1][-2] + m[2][-2] + m[2][-1]

        # Top right
        m[0][-1] = m[1][-2] + m[1][-1]

        # Go along the top
        # Second from top right
        m[0][-2] = m[0][-1] + m[1][-2] + m[1][-1]

        # Go along the top
        col = -3
        while col > -len(m[0]) + 1:
            print col
            new_val = m[0][col+1]  # Right
            new_val += m[1][col] # Below
            new_val += m[1][col+1] # Diagonal left
            new_val += m[1][col-1] # Diagonal right

            m[0][col] = new_val

            col -= 1


        # Second from top left

        # Top left


        print(m)
        # Go down the left
        # Go accross the bottom

        return m

    def matrix_max(m):
        return max(itertools.chain(*m))


    matrix = [[  5,  4,  2],
              [ 10,  1,  1],
              [ 11, 23, 25]]

    add_ring(matrix)
    # print(add_ring(matrix))

    assert add_ring(matrix) == [[147, 142, 133, 122,  59],
                                [304,   5,   4,   2,  57],
                                [330,  10,   1,   1,  54],
                                [351,  11,  23,  25,  26],
                                [362, 747, 806, 880, 931]]

    # while matrix_max(matrix) < i:
        # matrix = add_ring(matrix)


if __name__ == '__main__':
    p = 361527
    print(part_1(p))

    print(part_2(p))

