#! /usr/bin/python3
# -*- coding: utf-8 -*-

from is_map_search import *

s = MapNode.new_node("S")
a = MapNode.new_node("A", 21)
b = MapNode.new_node("B", 20)
c = MapNode.new_node("C", 12)
d = MapNode.new_node("D", 22)
e = MapNode.new_node("E", 8)
f = MapNode.new_node("F", 11)
g = MapNode.new_node("G", 0)

s.add_neighbour(a, 6)
s.add_neighbour(b, 9)
s.add_neighbour(d, 7)
a.add_neighbour(c, 7)
a.add_neighbour(d, 8)
b.add_neighbour(c, 8)
c.add_neighbour(e, 8)
d.add_neighbour(g, 10)
e.add_neighbour(f, 6)
e.add_neighbour(g, 8)
f.add_neighbour(g, 11)

print("Svemir (Depth-first search)")
TreeNode.children_sort_key = TreeNode.dist_sort
strategy = DepthFirstSearch()
strategy.search(s, g)

print("Svemir (Breadth-first search)")
TreeNode.children_sort_key = TreeNode.lex_sort
strategy = BreadthFirstSearch(True)
strategy.search(s, g)

print("Svemir (Best-first search)")
strategy = BestFirstSearch()
strategy.search(s, g)

print("Svemir (Branch-and-bound search)")
strategy = BranchAndBound(True)
strategy.search(s, g)

print("Svemir (A* search)")
strategy = AStarSearch()
strategy.search(s, g)