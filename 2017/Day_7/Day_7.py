#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections

class Tree(object):
    def __init__(self):
        self._list = []
        self._head = None

    def add(self, node):
        self._list.append(node)
        self.set_head()

    def get_head(self):
        self.set_head()
        
        if self._head is None:
            raise ValueError, 'Tree has no parent yet'
        return self._head

    def set_head(self):
        # Sets the first parentless node that it finds to be the head
        for node in self:
            if node.parent is None:
                self._head = node

    def __iter__(self):
        for n in self._list:
            yield n

    def search(self, N):
        for node in self._list:
            if node.name == N:
                return node

    def aggregate_weight(self, N):
        weight = 0
        for child in N.children:
            weight += self.aggregate_weight(child)

        return weight + N.weight


class Node(object):
    def __init__(self, name, weight, tree, children=None):
        self.name = name
        self.weight = int(weight)
        self.children = children or []
        self.parent = None

        self.link_children(tree)

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other

    def link_children(self, T):
        for child in self.children:
            node = T.search(child)
            if node is not None:
                node.parent = self

        T.set_head()

def create_tree(filename):
    tree = Tree()

    with open(filename) as f:
        for line in f.readlines():
            if '->' in line:
                name_and_weight, children = line.split('->')

            else:
                name_and_weight = line
                children = None

            name, weight = name_and_weight.translate(None, '()').strip().split(' ')
            children = [c.strip() for c in children.split(',')] if children else None

            n = Node(name, weight, tree, children)
            tree.add(n)

    for node in tree:
        node.link_children(tree)

    # Fix each node's list of children to be a list of nodes instead of a list of strings
    q = [tree.get_head()]
    while q:
        node = q.pop(0)
        if node.children:
            node.children = [tree.search(child) for child in node.children]
            q.extend(node.children)

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
    assert t.get_head() == 'tknk'
    assert part_2(t, search_tree(t)) == 60

    t = create_tree('input.txt')
    print('Part One:{}'.format(t.get_head()))
    print('Part Two:{}'.format(part_2(t, search_tree(t))))

