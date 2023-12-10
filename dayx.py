# import our helpers
from utils import show, Map, USING_EXAMPLE, NS, get_input_2023
from pathlib import Path
from dataclasses import dataclass
####### GLOBALS #########

# load todays input
TEXT = get_input_2023(Path(__file__))

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

if TEXT:
    PARSED = [A(*parse(_)) for _ in TEXT.splitlines()]
    #MAP = Map(TEXT.splitlines())
    #MAP.show()
    breakpoint()

# Visualize a 2D map
# import numpy as np
# ARRAY = np.zeros((z,y,x), dtype="uint8") # 3D Array
# ARRAY = np.zeros((y,x), dtype="uint8") # 2D Array
# for y, line in enumerate(TEXT):
#     ARRAY[y,:] = bytearray(line, "ascii")
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



######## Part 1 ##########
def p1(expect=0 if not USING_EXAMPLE else 0):
    return 0

######## Part 2 ##########
def p2(expect=0 if not USING_EXAMPLE else 0):
    return 0

##########################
if __name__ == "__main__":
    show(p1, p2)
