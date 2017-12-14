#!/usr/bin/env python
# -*- coding: utf-8 -*-

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


if __name__ == '__main__':
    tests = ((1, 0),
             (12, 3),
             (23, 2),
             (1024, 31))

    for i, o in tests:
        assert steps(i) == o, 'Steps for {} does not equal {} ({})'.format(i, o, steps(i))

    p = 361527
    print(steps(p))
