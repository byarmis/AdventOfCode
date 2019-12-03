#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_points(moves):
    points = []
    point = [0,0]

    for move in moves:
        direction, amt = move[0], int(move[1:])
        for _ in range(amt):
            if direction == 'U':
                point[0] += 1
            elif direction == 'D':
                point[0] -= 1
            elif direction == 'L':
                point[1] -= 1
            elif direction == 'R':
                point[1] += 1
            else:
                raise ValueError(f'Unknown direction: {direction}')
            points.append(tuple(point))

    return points

def part_1(moves_1, moves_2):
    points_1 = get_points(moves_1)
    points_2 = get_points(moves_2)

    intersections = sorted(list(set(points_1) & set(points_2)), key=lambda x: abs(x[0]) + abs(x[1]))

    print(f'Part one: {abs(intersections[0][0]) + abs(intersections[0][1])}')

def part_2(moves_1, moves_2):
    points_1 = get_points(moves_1)
    points_2 = get_points(moves_2)
    intersections = set(points_1) & set(points_2)

    steps = []
    for intersection in intersections:
        steps.append(points_1.index(intersection) + 1 
                    + points_2.index(intersection) + 1)

    print(f'Part two: {min(steps)}')


if __name__ == '__main__':
    with open('input.txt') as f:
        moves_1 = f.readline().split(',')
        moves_2 = f.readline().split(',')

    part_1(moves_1, moves_2)
    part_2(moves_1, moves_2)

