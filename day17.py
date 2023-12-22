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

H = len(TEXT)
W = len(TEXT[0])
MAP = np.zeros((H,W), dtype="uint8") # 2D Array
for Y, LINE in enumerate(TEXT):
    MAP[Y,:] = bytearray(LINE, "ascii")

#Map(MAP).show()

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

@dataclass
class Step:
    x: int
    y: int
    val: int
    prev: object

PATH1 = {
    0: [Step(0,0,0,None)]
}

P0 = Step(0,0,0,None)
P1 = Step(1,0,int(chr(MAP[0,1]))+P0.val,P0)
P2 = Step(2,0,int(chr(MAP[0,2]))+P1.val,P1)
P3 = Step(3,0,int(chr(MAP[0,3]))+P2.val,P2)
P4 = Step(4,0,int(chr(MAP[0,4]))+P3.val,P3)

PATH2 = {
    P4.val: [P4]
}

SEEN = set()

######## Part 1 ##########
def route(step):
    s = ""
    while step.prev:
        s += "x" if step.prev.x == step.x else "y"
        step = step.prev
    return s

def routexy(step,n):
    s = []
    while step:
        s.append((step.x,step.y))
        step = step.prev
        n -= 1
        if n == 0:
            return tuple(s)

def add_more_steps(PATH,step, val, p2):
    """."""
    y,x = step.y, step.x
    for (dy, dx) in ((1,0),(-1,0),(0,1),(0,-1)):
        # next pos candidate
        nx,ny = x+dx,y+dy

        # can't leave map
        if not 0<=ny<H:
            continue
        if not 0<=nx<W:
            continue

        sval = val + int(chr(MAP[ny,nx]))
        s = Step(nx,ny,sval,step)
        pth = route(s)

        # path already seen
        hsh = (x,y,routexy(s,3 if not p2 else 100))
        if hsh in SEEN:
            continue
        SEEN.add(hsh)

        # can't go backwards
        if step.prev and s.x == step.prev.x and s.y == step.prev.y:
            continue

        if p2:
            # can't go more than 10 steps
            if len(pth)>10 and len(set(pth[:11])) == 1:
                print(2,pth)
                continue

            # must go at least 3
            if len(set(pth[:3])) == 2:
                print(3,pth)
                continue
        else:
            # can't go more than 3 steps
            if len(pth)>3 and len(set(pth[:4])) == 1:
                continue

        if sval in PATH:
            PATH[sval].append(s)
        else:
            PATH[sval] = [s]

def shortest(PATH,p2=False):
    while True:
        val = min(PATH)
        step, *steps = PATH.pop(val)
        if steps:
            PATH[val] = steps
        if step.x == H-1 and step.y == W-1:
            return val
        #print(f"({step.x},{step.y}) = {val}")
        add_more_steps(PATH,step,val,p2)

def p1(expect=859 if not USING_EXAMPLE else 102):
    return shortest(PATH1, p2=False)

######## Part 2 ##########
def p2(expect=0 if not USING_EXAMPLE else 0):
    return shortest(PATH2, p2=True)

##########################
if __name__ == "__main__":
    show(p1, p2)
