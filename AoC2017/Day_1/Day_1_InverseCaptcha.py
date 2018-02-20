#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def inverse_captcha_p1(i):
    o = 0
    i = str(i)
    for first, second in zip(i, i[1:]):
        if first == second:
            o += int(first)
    if i[-1] == i[0]:
        o += int(i[0])
    return o


def inverse_captcha_p2(i):
    o = 0
    i = str(i)
    assert len(i) % 2 == 0, 'Length of input must be even'

    for first, second in zip(i, i[len(i) // 2 : ]):
        if first == second:
            o += int(first)

    return o * 2


def test(cases, f):
    r = True

    for i, expected in cases:
        ic = f(i)
        r &= ic == expected

    return r

if __name__ == '__main__':
    test_cases_p1 = ((1122, 3),
                    (1111, 4), 
                    (1234, 0),
                    (91212129, 9))

    r1 = test(test_cases_p1, inverse_captcha_p1)
    assert r1, 'First test cases fail'

    with open('input.txt') as f:
        p = int(f.readlines()[0])

    print('First solution:{}'.format(inverse_captcha_p1(p)))
    
    test_cases_p2 = ((1212, 6),
                     (1221, 0),
                     (123425, 4), 
                     (123123, 12),
                     (12131415, 4))
    
    r2 = test(test_cases_p2, inverse_captcha_p2)
    assert r2, 'Second test cases fail'

    print('Second solution:{}'.format(inverse_captcha_p2(p)))
