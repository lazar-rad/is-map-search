#! /usr/bin/python3
# -*- coding: utf-8 -*-

import math

box_hor = '─'
box_vert = '│'
box_vert_right = '├'
box_up_right = '└'
box_empty = ' '

def extend_down(si):
    so = ""
    for c in si:
        if c in [box_hor, box_up_right, box_empty]:
            so += box_empty
        elif c in [box_vert, box_vert_right]:
            so += box_vert
        else:
            so += box_empty
    return so



class MapNode:
    map_nodes = []

    def __init__(self, name, heuristics=0):
        self.name = name
        self.heuristics = heuristics
        self.neighbours = {}
        MapNode.map_nodes.append(self)
    
    def add_neighbour(self, m_node, distance=1):
        m_node = MapNode.get_node(m_node)
        if m_node == self:
            print("Can't add self as neighbour")
            return
        for neighbour in self.neighbours.keys():
            if neighbour == m_node:
                print("Neighbour already added")
                return
        self.neighbours[m_node] = distance
        m_node.neighbours[self] = distance
    
    def set_distance(self, m_node, distance):
        m_node = MapNode.get_node(m_node)
        neighbour = self.neighbour.get(m_node, None)
        if neighbour:
            neighbours[neighbour] = distance
        else:
            print("Neighbour not added")
    
    def is_neighbour(self, m_node):
        m_node = MapNode.get_node(m_node)
        return m_node in self.neighbours.keys()

    def distance_to(self, m_node):
        m_node = MapNode.get_node(m_node)
        return self.neighbours.get(m_node, math.inf)

    def new_node(name, heuristics=0):
        for m_node in MapNode.map_nodes:
            if m_node.name == name:
                print("Name already in use")
                return None
        return MapNode(name, heuristics)

    def get_node(name):
        if isinstance(name, MapNode):
            return name
        for m_node in MapNode.map_nodes:
            if m_node.name == name:
                return m_node
        return None



class TreeNode:
    expanded_nodes = 0
    lex_sort = lambda ch: ch.map_node.name
    dist_sort = lambda ch: ch.parent.map_node.distance_to(ch.map_node)
    children_sort_key = lex_sort

    def __init__(self, m_node):
        m_node = MapNode.get_node(m_node)
        self.map_node = m_node
        self.children = []
        self.parent = None
        self.expansion_order = 0
    
    def add_child(self, t_node):
        if (not t_node.parent) and not (t_node in self.children):
            self.children.append(t_node)
            t_node.parent = self
            self.children.sort(key=TreeNode.children_sort_key)

    def path(self):
        if self.parent:
            return self.parent.path() + " -> " + self.map_node.name
        else:
            return self.map_node.name

    def path_length(self):
        if self.parent:
            return self.parent.path_length() + self.parent.map_node.distance_to(self.map_node)
        else:
            return 0

    def cumulative_path_length(self):
        return self.path_length() + self.map_node.heuristics

    def visited(self, m_node):
        m_node = MapNode.get_node(m_node)
        if self.map_node == m_node:
            return True
        if not self.parent:
            return False
        return self.parent.visited(m_node)

    def expand(self, stop=None):
        if self.expansion_order == 0:
            TreeNode.expanded_nodes += 1
            self.expansion_order = TreeNode.expanded_nodes
            for m_node in self.map_node.neighbours:
                if not self.visited(m_node):
                    t_node = TreeNode(m_node)
                    self.add_child(t_node)
                    if m_node == stop:
                        return t_node
        else:
            print("Node already expanded")
        return None
    
    def check_as_expanded(self):
        if self.expansion_order == 0:
            TreeNode.expanded_nodes += 1
            self.expansion_order = TreeNode.expanded_nodes
        return None

    def __str__(self):
        s = self.map_node.name
        if self.expansion_order > 0:
            s += f"({self.expansion_order})"
        return s

    def to_string(self, show_lengths="", prefix=""):
        lengths = ""
        if ('p' in show_lengths) and ('h' in show_lengths):
            lengths = f"[{self.path_length()}+{self.map_node.heuristics}]"
        elif 'p' in show_lengths:
            lengths = f"[{self.path_length()}]"
        elif 'h' in show_lengths:
            lengths = f"[{self.map_node.heuristics}]"
        elif 'c' in show_lengths:
            lengths = f"[{self.path_length() + self.map_node.heuristics}]"
        s = prefix + str(self) + lengths + '\n'
        if len(self.children) > 0:
            prefix = extend_down(prefix)
            for ch in self.children[:-1]:
                s += ch.to_string(show_lengths, prefix + box_vert_right + box_hor)
            s += self.children[-1].to_string(show_lengths, prefix + box_up_right + box_hor)
        return s



class SearchStrategy:
    def __init__(self):
        self.t_node_list = []
        self.root = None
        self.show_lengths = ""
        self.start = None
        self.goal = None
        self.check_at_gen = False

    def search(self, start, goal):
        self.t_node_list = []
        self.start = MapNode.get_node(start)
        self.goal = MapNode.get_node(goal)
        self.root = TreeNode(start)
        self.t_node_list.append(self.root)
        t_node_final = self.root if self.start == self.goal else None
        while not t_node_final and len(self.t_node_list) > 0:
            t_node_final = self.search_step()
            if t_node_final:
                print(f"{t_node_final.path()} [{t_node_final.path_length()}]")
                self.print_tree()
                return
        print("Path not found")
        self.print_tree()

    def search_step(self):
        t_node = self.t_node_list.pop(0)
        if t_node.map_node == self.goal:
            t_node.check_as_expanded()
            return t_node
        m_node_check = self.goal if self.check_at_gen else None
        if self.worth_expanding(t_node):
            ret_t_node = t_node.expand(m_node_check)
            self.update_t_node_list(t_node)
            return ret_t_node
        return None

    def update_t_node_list(self, exp_t_node):
        pass
    
    def worth_expanding(self, t_node):
        return True

    def print_tree(self):
        print(self.root.to_string(self.show_lengths))



class DepthFirstSearch(SearchStrategy):
    def __init__(self):
        super().__init__()

    def update_t_node_list(self, exp_t_node):
        self.t_node_list = exp_t_node.children + self.t_node_list



class BreadthFirstSearch(SearchStrategy):
    def __init__(self, check_at_gen=False):
        super().__init__()
        self.check_at_gen = check_at_gen

    def update_t_node_list(self, exp_t_node):
        self.t_node_list += exp_t_node.children



class BestFirstSearch(SearchStrategy):
    def __init__(self, check_at_gen=False):
        super().__init__()
        self.show_lengths = "h"

    def update_t_node_list(self, exp_t_node):
        self.t_node_list += exp_t_node.children
        self.t_node_list.sort(key = lambda t_node: (t_node.map_node.heuristics, t_node.map_node.name))



class BranchAndBound(SearchStrategy):
    def __init__(self, dynamic=False):
        super().__init__()
        self.show_lengths = "p"
        self.dynamic = dynamic
        self.best_so_far = {}

    def update_t_node_list(self, exp_t_node):
        self.t_node_list += exp_t_node.children
        self.t_node_list.sort(key = lambda t_node: (t_node.path_length(), t_node.map_node.name))
        if self.dynamic:
            self.best_so_far[exp_t_node.map_node] = exp_t_node.path_length()

    def worth_expanding(self, t_node):
        return not self.dynamic or (t_node.path_length() <= self.best_so_far.get(t_node.map_node, math.inf))


class AStarSearch(SearchStrategy):
    def __init__(self):
        super().__init__()
        self.show_lengths = "ph"

    def update_t_node_list(self, exp_t_node):
        self.t_node_list += exp_t_node.children
        self.t_node_list.sort(key = lambda t_node: (t_node.cumulative_path_length(), t_node.map_node.name))


