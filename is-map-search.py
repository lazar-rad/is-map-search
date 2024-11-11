#! /usr/bin/python3
# -*- coding: utf-8 -*-

class MapNode:
    name = None
    heuristics = 1
    neighbours = {}

    def __init__(self, name, heuristics=1):
        self.name = name
        map_nodes.append(self)
        self.heuristics = heuristics
    
    def add_neighbour(self, node, distance=1):
        node = get_node(node)
        if node == self:
            print("Can't add self as neighbour")
            return
        for neighbour in self.neighbours.keys():
            if neighbour == node:
                print("Neighbour already added")
                return
        self.neighbours[node] = distance
    
    def set_distance(self, node, distance):
        node = get_node(node)
        neighbour = self.neighbour.get(node, None)
        if neighbour:
            neighbours[neighbour] = distance
        else:
            print("Neighbour not added")
    
    def is_neighbour(self, node):
        node = get_node(node)
        return node in self.neighbours.keys()

    def distance_to(self, node):
        node = get_node(node)
        return self.neighbours.get(node, infty)

map_nodes = []

def new_node(name):
    global map_nodes
    for node in map_nodes:
        if node.name == name:
            print("Name already in use")
            return None
    return MapNode(name)

def get_node(name):
    global map_nodes
    if isinstance(name, MapNode):
        return name
    for node in map_nodes:
        if node.name == name:
            return node
    return None


expanded_nodes = 0

class TreeNode:
    map_node = None
    parent = None
    children = []
    expansion_order = 0

    def __init__(self, node):
        node = get_node(node)
        self.map_node = node
    
    def add_child(self, tree_node):
        if (not tree_node.parent) and not (tree_node in self.children):
            self.children.append(tree_node)
            self.children.sort(key = lambda ch: ch.map_node.name)
    
    def path_length(self):
        if parent:
            return parent.path_length() + parent.distance_to(self)
        else:
            return 0
    
    def visited(self, node):
        node = get_node(node)
        if self.map_node == node:
            return True
        if not self.parent:
            return False
        return self.parent.visited(node)

    def expand(self):
        global expanded_nodes
        if self.expansion_order == 0:
            expanded_nodes += 1
            self.expansion_order = expanded_nodes
            for node in self.map_node.neighbours:
                if not self.visited(node):
                    self.add_child(TreeNode(node))
        else:
            print("Node already expanded")
    
    def __str__(self):
        s = self.map_node.name
        if self.expansion_order > 0:
            s += f" ({self.expansion_order})"
        return s

    def to_string(self, indent=0):
        s = indent*' ' + str(self) + '\n'
        for ch in self.children:
            s += ch.to_string(indent+1)
        return s


s = new_node("S")
a = new_node("A")
b = new_node("B")

s.add_neighbour(a, 8)
s.add_neighbour(b, 6)

tree = TreeNode(s)
tree.expand()
print(tree.to_string())