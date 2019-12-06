#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import lru_cache

class Solution:
    def __init__(self, f):
        self.tree = self.generate_tree(f)
        self.a = 'YOU'
        self.b = 'SAN'

    def generate_tree(self, links):
        tree = {}
        for link in links:
            target, source = link.strip().split(')')
            tree[source] = target

        return tree

    @lru_cache(maxsize=None)
    def get_cost(self, source):
        if source == 'COM':
            return 0
        return 1 + self.get_cost(self.tree[source])


    def part_1(self):
        s = sum(self.get_cost(source) for source in self.tree)
        print(f'Part 1:{s}')
        print(f'\tCache stats:{self.get_cost.cache_info()})')

    def find_common_node(self, a, b):
        possible_a = self.tree[a]
        possible_b = self.tree[b]

        while possible_a != possible_b:
            while possible_b != 'COM':
                if possible_b == possible_a:
                    return possible_a
                possible_b = self.tree[possible_b]
            possible_a = self.tree[possible_a]
            possible_b = self.tree[self.b]
        return possible_a
 
    def part_2(self):
        common_node = self.find_common_node(self.a, self.b)
        print(f'Common node: {common_node}')
        print(f'Part 2: {self.get_cost(self.a) + self.get_cost(self.b) - 2*self.get_cost(common_node) - 2}')

if __name__ == '__main__':
    with open('input.txt') as f:
        s = Solution(f.readlines())
    s.part_1()
    s.part_2()

