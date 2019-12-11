#!/usr/bin python3

def part_1():
    with open('input.txt') as f:
        f = f.readline().strip()

    width = 25
    height = 6

    zero_count = float('inf')
    min_mult = 0
    cnt = 0

    while cnt < len(f):
        layer = f[cnt:cnt+(width*height)]

        curr_zero_count = layer.count('0')
        if curr_zero_count < zero_count:
            min_mult = layer.count('1') * layer.count('2')
            zero_count = curr_zero_count

        cnt += width*height

    print(f'part 1: {min_mult}')

def part_2():
    with open('input.txt') as f:
        f = f.readline().strip()

    width = 25
    height = 6
    cnt = 0

    layers = []
    while cnt < len(f):
        layers.append(f[cnt:cnt+(width*height)])
        cnt += width*height

    output = [[None]*width]*height
    for w in range(width):
        for h in range(height):
            vertical_slice = (layer[w*h] for layer in layers[::-1])
            color = 2
            for val in vertical_slice:
                if int(val) < 2:
                    color = int(val)
                
            output[h][w] = color

    m = {0: '□',
         1: '■',
         2: ' ',
         }
    for layer in output:
        print(''.join(m[l] for l in layer))



part_1()
part_2()

