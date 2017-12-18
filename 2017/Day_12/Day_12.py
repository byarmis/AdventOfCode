#!/usr/bin/env python
# -*- coding: utf-8 -*-

def communicate_count(d, root_node=0):
    has_connections = {root_node} | d[0]

    changed = True
    while changed:
        changed = False
        for i in d:
            if i in has_connections:
                if d[i] - has_connections:
                    changed = True
                    has_connections |= d[i]

    return len(has_connections), has_connections

def group_count(d):
    groups = set()
    for root_node in d:
        _, connection_set = communicate_count(d, root_node)

        groups |= {tuple(sorted(list(connection_set)))}

    return len(groups)

def build_dict(filename):
    d = dict()
    with open(filename) as f:
        for line in f:
            node, connections = line.split('<->')
            connections = {int(c) for c in connections.split(',')}

            d[int(node)] = connections

    return d

if __name__ == '__main__':
    d = build_dict('test.txt')
    assert communicate_count(d)[0] == 6
    assert group_count(d) == 2

    d = build_dict('input.txt')
    print('Part One:{}'.format(communicate_count(d)[0]))
    print('Part Two:{}'.format(group_count(d)))

