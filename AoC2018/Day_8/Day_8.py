
def part_1r(input_str):
    input_list = list(map(int, input_str.split(' ')))

    meta = []

    def calc(idx):
        num_children = input_list[idx]
        num_metadata = input_list[idx+1]
        idx += 2

        for _ in range(num_children):
            idx = calc(idx)

        for i in range(num_metadata):
            meta.append(input_list[i + idx])

        return idx + num_metadata

    calc(0)

    return sum(meta)


test = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'

assert part_1(test) == 138

with open('input.txt') as f:
    print(part_1(f.readlines()[0]))

