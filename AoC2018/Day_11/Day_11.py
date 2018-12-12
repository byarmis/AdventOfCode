from itertools import chain

def get_pl(x, y, pi):
    '''
    Find the fuel cell's rack ID, which is its X coordinate plus 10.
    Begin with a power level of the rack ID times the Y coordinate.
    Increase the power level by the value of the grid serial number (your puzzle input).
    Set the power level to itself multiplied by the rack ID.
    Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
    Subtract 5 from the power level.
    '''

    i = (((x + 10) * y) + pi) * (x + 10)
    try:
        i = int(str(i)[-3])
    except IndexError:
        i = 0
    return i - 5

assert get_pl(3, 5, 8)      ==  4
assert get_pl(122, 79, 57)  == -5
assert get_pl(217, 196, 39) ==  0
assert get_pl(101, 153, 71) ==  4

grid = [[get_pl(x, y, 9810) for x in range(300)] for y in range(300)]
def part_1(puzzle_input, grid_size):
    cell_sum = 0
    max_coord=(0,0)
    for x in range(1, 300-grid_size+1):
        for y in range(1, 300-grid_size+1):
            cell_pl = 0
            for row in grid[x:x+grid_size]:
                cell_pl += sum(row[y:y+grid_size])

            if cell_pl > cell_sum:
                cell_sum = cell_pl
                max_coord = (y, x)

    return max_coord, cell_sum

print(part_1(18,3)[0])
#assert part_1(18, 3)[0] == (33,45)
print('Part 1', part_1(9810, 3))

def part_2(puzzle_input):
    m = 0
    for gs in range(1, 301):
        print(gs)
        p1 = part_1(puzzle_input, gs)
        if p1[1] > m:
            m_gs = gs
            m_cd = p1[0]
    return m_cd , m_gs


print(part_2(9810))
assert part_2(18) == (90,269,16)
assert part_2(42) == (232,251,12)

