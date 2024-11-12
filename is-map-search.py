#! /usr/bin/python3
# -*- coding: utf-8 -*-

import math

class MapNode:
#    name = None
#    heuristics = 1
#    neighbours = {}
    map_nodes = []

    def __init__(self, name, heuristics=1):
        self.name = name
        self.heuristics = heuristics
        self.neighbours = {}
        MapNode.map_nodes.append(self)
    
    def add_neighbour(self, node, distance=1):
        node = MapNode.get_node(node)
        if node == self:
            print("Can't add self as neighbour")
            return
        for neighbour in self.neighbours.keys():
            if neighbour == node:
                print("Neighbour already added")
                return
        self.neighbours[node] = distance
        node.neighbours[self] = distance
    
    def set_distance(self, node, distance):
        node = MapNode.get_node(node)
        neighbour = self.neighbour.get(node, None)
        if neighbour:
            neighbours[neighbour] = distance
        else:
            print("Neighbour not added")
    
    def is_neighbour(self, node):
        node = MapNode.get_node(node)
        return node in self.neighbours.keys()

    def distance_to(self, node):
        node = MapNode.get_node(node)
        return self.neighbours.get(node, math.inf)

    def new_node(name):
        for node in MapNode.map_nodes:
            if node.name == name:
                print("Name already in use")
                return None
        return MapNode(name)

    def get_node(name):
        if isinstance(name, MapNode):
            return name
        for node in MapNode.map_nodes:
            if node.name == name:
                return node
        return None



class TreeNode:
    #map_node = None
    #parent = None
    #children = []
    #expansion_order = 0
    expanded_nodes = 0

    def __init__(self, node):
        node = MapNode.get_node(node)
        self.map_node = node
        self.children = []
        self.parent = None
        self.expansion_order = 0
    
    def add_child(self, tree_node):
        if (not tree_node.parent) and not (tree_node in self.children):
            self.children.append(tree_node)
            tree_node.parent = self
            self.children.sort(key = lambda ch: ch.map_node.name)
    
    def path_length(self):
        if self.parent:
            return self.parent.path_length() + self.parent.map_node.distance_to(self.map_node)
        else:
            return 0
    
    def path(self):
        if self.parent:
            return self.parent.path() + " -> " + self.map_node.name
        else:
            return self.map_node.name
    
    def visited(self, node):
        node = MapNode.get_node(node)
        if self.map_node == node:
            return True
        if not self.parent:
            return False
        return self.parent.visited(node)

    def expand(self):
        if self.expansion_order == 0:
            TreeNode.expanded_nodes += 1
            self.expansion_order = TreeNode.expanded_nodes
            for node in self.map_node.neighbours:
                if not self.visited(node):
                    self.add_child(TreeNode(node))
            s_ch = ""
            for ch in self.children:
                s_ch += str(ch) + ' '
            print(f"Expanded {str(self)} [{s_ch.strip()}]")
        else:
            print("Node already expanded")
    
    def __str__(self):
        s = self.map_node.name
        if self.expansion_order > 0:
            s += f"({self.expansion_order})"
        return s

    def to_string(self, indent=0):
        s = indent*' ' + str(self) + '\n'
        for ch in self.children:
            s += ch.to_string(indent+1)
        return s

class SearchStrategy:
    nodes_to_visit = []

    def __init__(self):
        pass

    def search(self, start, goal):
        start = MapNode.get_node(start)
        goal = MapNode.get_node(goal)
        root = TreeNode(start)
        SearchStrategy.nodes_to_visit.append(root)
        while len(SearchStrategy.nodes_to_visit) > 0:
            node = SearchStrategy.nodes_to_visit.pop(0)
            node.expand()
            SearchStrategy.nodes_to_visit += node.children
            if node.map_node == goal:
                print(f"{node.path()} ({node.path_length()})")
                print(root.to_string())
                return
        print("Path not found")
        print(root.to_string())


s = MapNode.new_node("S")
a = MapNode.new_node("A")
b = MapNode.new_node("B")
c = MapNode.new_node("C")
d = MapNode.new_node("D")
e = MapNode.new_node("E")
f = MapNode.new_node("F")
g = MapNode.new_node("G")

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

strategy = SearchStrategy()
strategy.search(s, g)