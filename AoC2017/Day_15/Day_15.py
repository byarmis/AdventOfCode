#!/usr/bin/env python
# -*- coding: utf-8 -*-

def progress (iteration, total):
    """
    Call in a loop to create terminal progress bar
    https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
    """
    prefix = ''
    suffix = ''
    length = 100
    fill = '█'

    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)

    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')

    # Print New Line on Complete
    if iteration == total: 
        print()

class Generator:
    def __init__(self, start, factor, product=2147483647, m=1):
        self.previous = start
        self.factor = factor
        self.product = product
        self.multiple = m

        self._eq = None

    def __next__(self):
        self.previous = (self.previous * self.factor) % self.product
        while self.previous % self.multiple != 0:
            self.previous = (self.previous * self.factor) % self.product

        self._eq = self.previous & 0xFFFF
        return self.previous

    def __eq__(self, other):
        return self._eq == other._eq

def counts(a_start, b_start, r, m=(1,1)):
    A = Generator(start=a_start, factor=16807, m=m[0])
    next(A)

    B = Generator(start=b_start, factor=48271, m=m[1])
    next(B)

    c = 0

    for _ in range(r):
        progress(_, r-1) if _ % (r//min(r, 1000)) < 2 else None

        if A == B:
            c += 1
        next(A)
        next(B)

    return c


if __name__ == '__main__':
    A = Generator(start=65, factor=16807)
    B = Generator(start=8921, factor=48271)

    a_test = (
            1092455
          , 1181022009
          , 245556042
          , 1744312007
          , 1352636452
    )

    b_test = (
              430625591
            , 1233683848
            , 1431495498
            , 137874439
            , 285222916
    )

    for a in a_test:
        assert a == next(A)

    for b in b_test:
        assert b == next(B)

    
    c = counts(65, 8921, 5)
    assert c == 1, '{} != 1'.format(c)

    c = counts(65, 8921, 40000000)
    assert c == 588, '{} != 588'.format(c)

    c = counts(679, 771, 40000000)
    print('\nPart One:{}'.format(c))

    c = counts(679, 771, 5000000, m=(4, 8))
    print('\nPart Two:{}'.format(c))

