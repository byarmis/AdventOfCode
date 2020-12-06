class Seat:
    def __init__(self, s):
        self.s = s.strip()

    def row(self):
        s = self.s[:7]
        s = s.replace('F', '0')
        s = s.replace('B', '1')

        return int(s, 2)


    def column(self):
        s = self.s[-3:]
        s = s.replace('R', '1')
        s = s.replace('L', '0')

        return int(s, 2)

    def ID(self):
        return self.row() * 8 + self.column()

with open('input.txt') as f:
    seats = [Seat(s) for s in f.readlines()]

print('Part one: ', max(s.ID() for s in seats))

allocated_seats = [[False]*8 for _ in range(128)]

for seat in seats:
    allocated_seats[seat.row()][seat.column()] = True

trimmed = allocated_seats[12:-17]

for row_num, row in enumerate(trimmed):
    if False in row:
        for col_num, col in enumerate(row):
            if not col:
                my_id = (row_num + 12) * 8 + col_num 
                print('Part two: ', my_id)

