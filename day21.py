""" day x """
from pathlib import Path
from dataclasses import dataclass
import numpy as np
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

# Visualize a 2D map
H = len(TEXT)
W = len(TEXT[0])
ARRAY = np.zeros((H,W), dtype="uint8") # 2D Array
for Y, LINE in enumerate(TEXT):
    ARRAY[Y,:] = bytearray(LINE, "ascii")
YX = list(zip(*np.where(ARRAY==ord("S"))))

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

GARDEN = ord(".")
ROCK = ord("#")
ARRAY[YX[0][0],YX[0][1]] = GARDEN

######## Part 1 ##########
def fn():
    """."""

def p1(expect=3853 if not USING_EXAMPLE else 16):
    poss = set(YX)
    for _ in range(55 if not USING_EXAMPLE else 6):
        nposs = set()
        for yx in poss:
            y,x = yx
            for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                if ARRAY[y+dy,x+dx] == GARDEN:
                    nposs.add((y+dy,x+dx))
        poss = nposs
    for y,x in nposs:
        ARRAY[y,x] = 1
    Map(ARRAY).show()
    return len(nposs)

######## Part 2 ##########
def p2(expect=0 if not USING_EXAMPLE else 0):
    """
    from map shown at end of part 1:
    reachable squares are a rotated checkerboard
    """
    return 0

##########################
if __name__ == "__main__":
    show(p1, p2)
