from collections import deque

test_inputs = [
    ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 7),
    ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5), 
    ('nppdvjthqldpwncqszvftbrmjlhg', 6), 
    ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10), 
    ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11), 
]

def part_1(line: str, num:int) -> int:
    d = deque(maxlen=num)

    for _ in range(num):
        d.append(line[0])
        line = line[1:]
    
    c = num
    while len(set(d)) != num:
        d.append(line[0])
        line = line[1:]
        c += 1

    return c


if __name__ == '__main__':
    with open('input.txt') as f:
        line = f.readline()

    for test_input, test_output in test_inputs:
        assert part_1(test_input, 4) == test_output

    print('Part 1: ', part_1(line, 4))
    print('Part 2: ', part_1(line, 14))

