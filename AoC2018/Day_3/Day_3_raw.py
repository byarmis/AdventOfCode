with open('input.txt') as f:
    lines = f.readlines()

import re
R = r'#(\d*) @ (\d*),(\d*): (\d*)x(\d*)'

claimed = set()
claimed_id_set = set()
overlap = 0
from collections import defaultdict
claimed_id_dd = defaultdict(set)

for line in lines:
    line_parsed = re.match(R, line)

    ID = int(line_parsed.group(1))
    x_start = int(line_parsed.group(2))
    y_start = int(line_parsed.group(3))
    width = int(line_parsed.group(4))
    height = int(line_parsed.group(5))

    X = range(x_start, x_start+width)
    Y = range(y_start, y_start+height)

    claimed_id_set.add(ID)

    for x in X:
        for y in Y:
            for overlapping_id in claimed_id_dd[(x,y)]:
                claimed_id_set.discard(overlapping_id)
                claimed_id_set.discard(ID)

            claimed_id_dd[(x,y)].add(ID)

print(sum(1 for v in claimed_id_dd.values() if len(v)>1))
print(claimed_id_set)

