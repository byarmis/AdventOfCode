#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections
import re
from functools import lru_cache

class Tree(object):
    def __init__(self):
        self._dict = {}
        self._head = None

    def add(self, node):
        self._dict[node.name] = node

    def get_head(self):
        if self._head is None:
            raise ValueError('Tree has no head yet')
        return self._head

    def set_head(self):
        # Sets the first parentless node that it finds to be the head
        for node in self:
            if node.parent is None:
                self._head = node
                return

    def __iter__(self):
        return iter(self._dict.values())

    def search(self, N):
        return self._dict[N]

    @lru_cache(maxsize=None)
    def aggregate_weight(self, N):
        weight = N.weight
        for child in N.children:
            weight += self.aggregate_weight(child)
        return weight 


class Node(object):
    def __init__(self, name, weight, tree, children=None):
        r = r'.*\((\d*)\).*'
        self.weight = int(re.match(r, weight).group(1))

        self.name = name
        self.children = children or []
        self.parent = None
        self._hash = hash(self.name)

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other

    def __hash__(self):
        return self._hash


def create_tree(filename):
    tree = Tree()

    with open(filename) as f:
        for line in f.readlines():
            if '->' in line:
                name_and_weight, children = line.split('->')

            else:
                name_and_weight = line
                children = ''

            name, weight = name_and_weight.strip().split(' ')
            children = [c.strip() for c in children.split(',') if c] 

            n = Node(name, weight, tree, children)
            tree.add(n)

    # Fix each node's list of children to be a list of nodes instead of a list of strings
    for node in tree:
        node.children = [tree.search(child) for child in node.children]

        for child in node.children:
            child.parent = node

    tree.set_head()

    return tree

def mode(data):
    cnt = collections.Counter(data)

    m = max(cnt.values())
    for d in data:
        if cnt[d] == m:
            return d

def siblings_weights(T, N):
    return {T.aggregate_weight(child) for child in N.parent.children}

def search_tree(T):
    '''
    Returns the root node of the sub-tree that is the wrong weight and it's sibiling's weights
    '''
    node = T.get_head()

    # While a node is imbalanced, follow that node
    while True:
        child_weights = {child:T.aggregate_weight(child) for child in node.children}
        layer_mode = mode(child_weights.values())

        wrong_weight = [child for child in child_weights if child_weights[child] != layer_mode]

        if wrong_weight:
            node = wrong_weight[0]
        else:
            break

    return node

def part_2(tree, node):
    right_weight = next(iter(siblings_weights(t, node) - {tree.aggregate_weight(node)}))
    weight_diff = right_weight - tree.aggregate_weight(node)

    return node.weight + weight_diff

if __name__ == '__main__':
    t = create_tree('test.txt')
    assert t.get_head() == 'tknk', 'Expected {}, got {}'.format('tknk', t.get_head())
    assert part_2(t, search_tree(t)) == 60
    t = create_tree('input.txt')

    print('Part One:{}'.format(t.get_head()))
    print('Part Two:{}'.format(part_2(t, search_tree(t))))

