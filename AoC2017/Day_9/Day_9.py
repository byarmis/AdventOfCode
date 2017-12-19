#!/usr/bin/env python
# -*- coding: utf-8 -*-

def score(str_in):
    garbage = False
    cnt = 1
    out = 0
    stack = []
    garbage_cnt = 0

    skip = False

    for i in str_in:
        if skip:
            skip = False
            continue

        if i == '!':
            skip = True
            continue

        if garbage and i == '>':
            garbage = False

        if garbage:
            garbage_cnt += 1
            continue

        if i == '<' and not garbage:
            garbage = True

        if i == '{':
            stack.append(cnt)
            cnt += 1

        elif i == '}':
            popped = stack.pop()
            out += popped
            cnt -= 1

    return out, garbage_cnt

if __name__ == '__main__':
    with open('score.txt') as f:
        test_lines = f.readlines()

    for line in test_lines:
        test_input, expected_output = line.split('\\')
        expected = int(expected_output)

        assert score(test_input)[0] == expected, 'String:{}\tExpected:{}\tActual:{}'.format(test_input[0], expected, score(test_input))

    with open('input.txt') as f:
        line = f.readline().strip()

    print(score(line))

