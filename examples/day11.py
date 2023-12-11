# import our helpers
from utils import show, Map, USING_EXAMPLE, NS, get_input_2023
from pathlib import Path
from dataclasses import dataclass
from itertools import combinations

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
class A:
    a : str
    b : int
    c : list

#if TEXT:
    #PARSED = [A(*parse(_)) for _ in TEXT]
    #MAP = Map(TEXT)
    #MAP.show()
    #breakpoint()

# Visualize a 2D map
import numpy as np
# ARRAY = np.zeros((z,y,x), dtype="uint8") # 3D Array
H = len(TEXT)
W = len(TEXT[0])
ARRAY = np.zeros((H,W), dtype="uint8") # 2D Array
for y, line in enumerate(TEXT):
    ARRAY[y,:] = bytearray(line, "ascii")


# ARRAY_SLICE = ARRAY[0:2,0:3,22:26] # 2 layers, 3 rows, 4 columns
# ARRAY_SLICE = ARRAY[0:2,:,22:26] # 2 layers, all rows, 4 columns
# Map(ARRAY_SLICE).show()

# Build a network graph
from networkx.algorithms.shortest_paths.astar import astar_path_length
import networkx as nx
import networkx.drawing.nx_pylab as nd
import matplotlib.pyplot as plt
G = nx.Graph() # just in case one way paths exist...
#G = nx.from_numpy_array(ARRAY)
GALAXIES = []
for y in range(H):
    for x in range(W):
        G.add_node((y,x))
        if ARRAY[y,x] == ord("#"):
            GALAXIES.append((y,x))

def xweight(x):
    if len(set(ARRAY[:,x])) == 1:
        return 2
    return 1

def yweight(y):
    if len(set(ARRAY[y,:])) == 1:
        return 2
    return 1

for y in range(H):
    for x in range(W):
        if y+1 < H:
            G.add_edge((y,x),(y+1,x),weight=yweight(y+1))
        if x+1 < W:
            G.add_edge((y,x),(y,x+1),weight=xweight(x+1))

#breakpoint()
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
# nx.shortest_path(G, "A", "D", weight="weight")
# ['A', 'B', 'D']

#nd.draw_networkx(G) # show network
#plt.show() # draw



######## Part 1 ##########
def p1(expect=0 if not USING_EXAMPLE else 0):
    from networkx.classes.function import path_weight
    acc = 0
    for src, dst in combinations(GALAXIES,2):
        path = nx.shortest_path(G, src, dst, weight="weight")
        n = path_weight(G, path, weight="weight")
        print(src, dst, n)
        acc += n

    return acc

######## Part 2 ##########
def p2(expect=0 if not USING_EXAMPLE else 0):
    return 0

##########################
if __name__ == "__main__":
    show(p1, p2)
