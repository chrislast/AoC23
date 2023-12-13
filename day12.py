"""day 12"""
from pathlib import Path
from dataclasses import dataclass
import numpy as np
# import networkx as nx
# from nx.algorithms.shortest_paths.astar import astar_path_length
# import nx.drawing.nx_pylab as nd
# import matplotlib.pyplot as plt
# from collections import deque, Counter
# from itertools import combinations, permutations
from utils import show, Map, USING_EXAMPLE, NS, get_input_2023
####### GLOBALS #########

# load todays input
TEXT = get_input_2023(Path(__file__)).splitlines()

# parse the input (usually)
# def parse(line):
#     """
#     fmt
#     """
#     a,b,*c = line.split()
#     return a, int(b[:-1]), ' '.join(c)

# @dataclass
# class A:
#     a : str
#     b : int
#     c : list

# if TEXT:
#     PARSED = [A(*parse(_)) for _ in TEXT]
#     #MAP = Map(TEXT)
#     #MAP.show()
#     breakpoint()

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
# from networkx.algorithms.shortest_paths.astar import astar_path_length
# import networkx.drawing.nx_pylab as nd
# import matplotlib.pyplot as plt
# G = nx.DiGraph() # just in case one way paths exist...
# G.add_nodes_from(listofstring?)
# for node in G.nodes:
#     G.nodes[node].update(dict(property=val))
#     for dest in listofdestnodes:
#         G.add_edge(node,dest)

# >>> import networkx as nx
# >>> G = nx.Graph()
# >>> G.add_edge("A", "B", weight=4)
# >>> G.add_edge("B", "D", weight=2)
# >>> G.add_edge("A", "C", weight=3)
# >>> G.add_edge("C", "D", weight=4)
# >>> nx.shortest_path(G, "A", "D", weight="weight")
# ['A', 'B', 'D']

# nd.draw_networkx(G) # show network
# plt.show() # draw
INVALID = 9999
######## Part 1 ##########

def recursive_count(txt, tgt):
    if "?" in txt:
        pos = txt.index("?")
        s = txt[:pos]
        e = txt[pos+1:]
        return recursive_count(s+"."+e,tgt) + recursive_count(s+"#"+e,tgt)
    return 1 if [len(_) for _ in txt.split(".") if _] == tgt else 0

def p1(expect=7379 if not USING_EXAMPLE else 21):
    acc = 0
    for line in TEXT:
        ptn, cnt = line.split()
        tgt = list(map(int,cnt.split(",")))
        acc += recursive_count2(ptn,tgt)
    return acc

######## Part 2 ##########
def recursive_count2(txt, tgt):
    #print(txt,tgt)
    # remove full matches
    groups = [_ for _ in txt.split(".") if _]
    for g,l in zip(groups,tgt):
        if "?" in g:
            break
        if g != "#"*l:
            return 0
    if "?" in txt:
        pos = txt.index("?")
        s = txt[:pos]
        e = txt[pos+1:]
        return recursive_count2(s+"."+e,tgt) + recursive_count2(s+"#"+e,tgt)
    return 1 if [len(_) for _ in txt.split(".") if _] == tgt else 0

from functools import cache

def p2(expect=7732028747925 if not USING_EXAMPLE else 102050):
    acc = 0
    for n,line in enumerate(TEXT):
        print(n,acc,line)
        ptn, cnt = line.split()
        tgt = list(map(int,cnt.split(",")))
        acc += recursive_count2(ptn*5,tgt*5)
    return acc

def p2cheat():
    from re import match
    return sum((g:=cache(lambda m,d: not d if not m else (m[0]!='#' and g(m[1:],d))+(d and match(r'[#?]{%d}[.?]'%d[0],m) and g(m[d[0]+1:],d[1:]) or 0)))('?'.join([s[0]]*5)+'.',(*map(int,s[1].split(',')),)*5) for s in map(str.split,TEXT))

##########################
if __name__ == "__main__":
    show(p1, p2)
