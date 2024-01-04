""" day 23 """
from pathlib import Path
import numpy as np
import networkx as nx
from utils import show, USING_EXAMPLE, get_input_2023
####### GLOBALS #########

# load todays input
TEXT = get_input_2023(Path(__file__)).splitlines()
H = len(TEXT)
W = len(TEXT[0])
ARRAY = np.zeros((H,W), dtype="uint8") # 2D Array
for Y, LINE in enumerate(TEXT):
    ARRAY[Y,:] = bytearray(LINE, "ascii")

TREE = ord("#")
PATH = ord(".")
LTOR = ord(">")
RTOL = ord("<")
UTOD = ord("v")
DTOU = ord("^")
START = (0,1)
END = (H-1,W-2)

NODES = {(y,x):ARRAY[y,x] for x in range(W) for y in range(H)
         if ARRAY[y,x] in (PATH,LTOR,RTOL,UTOD,DTOU)}

######## Part 1 ##########
# Build a network graph
G = nx.DiGraph() # just in case one way paths exist...
G.add_nodes_from(n for n in NODES)
#for YX in NODES:
for NODE in NODES:
    y,x = NODE
    if ARRAY[y,x] == LTOR:
        G.add_edge(NODE,(y,x+1))
    elif ARRAY[y,x] == RTOL:
        G.add_edge(NODE,(y,x-1))
    elif ARRAY[y,x] == UTOD:
        G.add_edge(NODE,(y+1,x))
    elif ARRAY[y,x] == DTOU:
        G.add_edge(NODE,(y-1,x))
    else:
        for dy,dx,exc in ((0,1,"<"),(0,-1,">"),(1,0,"^"),(-1,0,"v")):
            pos = (y+dy,x+dx)
            if pos in NODES and NODES[pos] not in (exc,"#"):
                G.add_edge(NODE,pos)

def p1(expect=2134 if not USING_EXAMPLE else 94):
    "11 seconds makes part 2 concerning!"
    paths = nx.all_simple_paths(G, source=START, target=END)
    return max(len(p)-1 for p in paths)

######## Part 2 ##########
G2 = nx.DiGraph() # just in case one way paths exist...
G2.add_nodes_from(n for n in NODES)
for NODE in NODES:
    y,x = NODE
    for dy,dx in ((0,1),(0,-1),(1,0),(-1,0)):
        pos = (y+dy,x+dx)
        if pos in NODES and NODES[pos] != "#":
            G2.add_edge(NODE,pos)

def dfs(pth):
    y,x = pth[-1]
    if (y,x) == END:
        print(len(pth))
        return len(pth)
    acc = []
    for dy,dx in ((0,1),(0,-1),(1,0),(-1,0)):
        npos = (y+dy,x+dx)
        if npos not in pth and ARRAY[y+dy,x+dx] != TREE:
            acc.append(dfs(pth + [npos]))
    if not acc:
        return 0
    return max(acc)

import sys
sys.setrecursionlimit(9999)
def p2(expect=1 if not USING_EXAMPLE else 154):
    return dfs([(0,1),(1,1)])-1

##########################
if __name__ == "__main__":
    show(p1, p2)
