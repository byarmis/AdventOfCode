#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Tree(object):
    def __init__(self):
        self._list = []
        self._head = None

    def add(self, node):
        self._list.append(node)
        self.set_head()

    def get_head(self):
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

class Node(object):
    def __init__(self, name, weight, tree, children=None):
        self.name = name
        self.weight = weight
        self.children = children or []
        self.parent = None

        self.link_children(tree)

    def __str__(self):
        return self.name

    def link_children(self, T):
        for child in self.children:
            for node in T:
                if node.name == child:
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

    return tree

if __name__ == '__main__':
    t = create_tree('test.txt')
    assert str(t.get_head()) == 'tknk'

    t = create_tree('input.txt')
    print(t.get_head())

