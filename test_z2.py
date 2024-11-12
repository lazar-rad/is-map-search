#! /usr/bin/python3
# -*- coding: utf-8 -*-

from is_map_search import *

s = MapNode.new_node("S")
a = MapNode.new_node("A", 5)
b = MapNode.new_node("B", 6)
c = MapNode.new_node("C", 8)
d = MapNode.new_node("D", 9)
e = MapNode.new_node("E", 5)
f = MapNode.new_node("F", 2)
g = MapNode.new_node("G", 0)

s.add_neighbour(a, 2)
s.add_neighbour(b, 4)
a.add_neighbour(c, 4)
a.add_neighbour(e, 1)
b.add_neighbour(g, 11)
c.add_neighbour(d, 1)
c.add_neighbour(e, 1)
c.add_neighbour(f, 3)
e.add_neighbour(g, 10)
f.add_neighbour(g, 2)

#tree = TreeNode(s)
#tree.expand()
#print(tree.to_string())

#strategy = SearchStrategy()
strategy = DepthFirstSearch()
#strategy = BreadthFirstSearch(True)
#strategy = BestFirstSearch()
#strategy = BranchAndBound()
#strategy = AStarSearch()

strategy.show_lengths="p"
TreeNode.children_sort_key = TreeNode.dist_sort
strategy.search(s, g)