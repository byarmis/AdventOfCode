
with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

def part_1(lines):
    seeds = lines.pop(0)
    label, seeds = seeds.split(':')
    seeds = [int(s) for s in seeds.split()]

    _ = lines.pop(0)

    class Map:
        def __init__(self, lines):
            self.lines = []
            self.name = lines.pop(0)[:-1]

            for line in lines:
                dest, source, length = line.split()
                dest = int(dest)
                source = int(source)
                length = int(length)

                self.lines.append((source, dest, length))

        def __getitem__(self, item):
            for line in self.lines:
                source, dest, length = line
                if source <= item <= source + length:
                    return dest + (item - source)

            return item

        def __repr__(self):
            return self.name

        def __len__(self):
            return len(self.lines)

    m = []
    line_chunk = []
    for line in lines:
        if not line.strip():
            m.append(Map(line_chunk))
            line_chunk = []
        else:
            line_chunk.append(line)

    min_loc = float('inf')

    for seed in seeds:
        val = m[5][m[4][m[3][m[2][m[1][m[0][seed]]]]]]
        min_loc = min(val, min_loc)

    return min_loc

test_lines = [
        'seeds: 79 14 55 13',
'',
        'seed-to-soil map:',
        '50 98 2',
        '52 50 48',
'',
        'soil-to-fertilizer map:',
        '0 15 37',
        '37 52 2',
        '39 0 15',
'',
        'fertilizer-to-water map:',
        '49 53 8',
        '0 11 42',
        '42 0 7',
        '57 7 4',
'',
        'water-to-light map:',
        '88 18 7',
        '18 25 70',
'',
        'light-to-temperature map:',
        '45 77 23',
        '81 45 19',
        '68 64 13',
'',
        'temperature-to-humidity map:',
        '0 69 1',
        '1 0 69',
'',
        'humidity-to-location map:',
        '60 56 37',
        '56 93 4',
        ]

assert part_1(test_lines) == 35
p1 = part_1(lines)
assert p1 != 550841242
print(p1)

