#! /usr/bin/python3
# -*- coding: utf-8 -*-

nodes = []
node_start = None
node_goal = None
distances = {}
heuristics = None

def parse_input(fn_in):
    INIT = 0
    NODES = 1
    NODE_START = 2
    NODE_GOAL = 3
    GRAPH = 4
    HEURISTICS = 5
    global nodes
    global node_start
    global node_goal
    global graph
    global heuristics
    file_in = open(fn_in, 'r')
    s = file_in.read().split('\n')
    file_in.close()
    line_cnt = 0
    graph_line_cnt = 0
    for line_ in s:
        line = line_.strip()
        if len(line) == 0 or line[0] == '#':
            continue
        if state == INIT:
            if line == "nodes:":
                state = NODES
            elif line == "start:":
                state = NODE_START
            elif line == "goal":
                state = NODE_GOAL
            elif line in ["graph:", "table:"]:
                state = GRAPH
            elif line in ["heur:", "heuristics:"]:
                state = HEURISTICS
            else:
                print(f"!!! Error on line {line_cnt}")
                exit()
        elif state = NODES:
            nodes = line.split()
            state = INIT
        elif state = NODE_START:
            node_start = line[:]
            if not node_start in nodes:
                print(f"!!! Error on line {line_cnt}")
                exit()
        elif state = NODE_GOAL:
            node_goal = line[:]
            if not node_goal in nodes:
                print(f"!!! Error on line {line_cnt}")
                exit()
        elif state = GRAPH:
            graph_line = line.split()
            if len(graph_line) > 0 and graph_line[0] == 