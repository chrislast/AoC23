""" day x """
from pathlib import Path
from dataclasses import dataclass
# import numpy as np
# import networkx as nx
# from nx.algorithms.shortest_paths.astar import astar_path_length
# import nx.drawing.nx_pylab as nd
# import matplotlib.pyplot as plt
# from collections import deque, Counter
# from itertools import combinations, permutations
# import re
# from functools import cache
from utils import show, Map, USING_EXAMPLE, NS, get_input_2023
####### GLOBALS #########

# load todays input
TEXT = get_input_2023(Path(__file__)).splitlines()

# parse the input (usually)
def parse(line):
    """
    fmt
    """
    a,b,*c = line.split()
    return a, int(b[:-1]), ' '.join(c)

@dataclass
class Thing:
    """Input"""
    a : str
    b : int
    c : list

if TEXT:
    THINGS = [Thing(*parse(_)) for _ in TEXT]
    #MAP = Map(TEXT)
    #MAP.show()

# Visualize a 2D map
# ARRAY = np.zeros((z,y,x), dtype="uint8") # 3D Array
# H = len(TEXT)
# W = len(TEXT[0])
# ARRAY = np.zeros((H,W), dtype="uint8") # 2D Array
# for y, line in enumerate(TEXT):
#     ARRAY[y,:] = bytearray(line, "ascii")
# YX = list(zip(*np.where(ARRAY==ord("S"))))
# ARRAY_SLICE = ARRAY[0:2,0:3,22:26] # 2 layers, 3 rows, 4 columns
# ARRAY_SLICE = ARRAY[0:2,:,22:26] # 2 layers, all rows, 4 columns
# Map(ARRAY_SLICE).show()

# Build a network graph
# G = nx.DiGraph() # just in case one way paths exist...
# G.add_nodes_from(listofstring?)
# for node in G.nodes:
#     G.nodes[node].update(dict(property=val))
#     for dest in listofdestnodes:
#         G.add_edge(node,dest)

# >>> G = nx.Graph()
# >>> G.add_edge("A", "B", weight=4)
# >>> G.add_edge("B", "D", weight=2)
# >>> G.add_edge("A", "C", weight=3)
# >>> G.add_edge("C", "D", weight=4)
# >>> nx.shortest_path(G, "A", "D", weight="weight")
# ['A', 'B', 'D']

# nd.draw_networkx(G) # show network
# plt.show() # draw

######## Part 1 ##########
def fn():
    """."""

def p1(expect=0 if not USING_EXAMPLE else 0):
    breakpoint()
    return 0

######## Part 2 ##########
def p2(expect=0 if not USING_EXAMPLE else 0):
    return 0

##########################
if __name__ == "__main__":
    show(p1, p2)
