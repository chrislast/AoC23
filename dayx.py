# import our helpers
from types import SimpleNamespace
from utils import load, show, TRACE, Map, Path, USING_EXAMPLE
from pathlib import Path
from dataclasses import dataclass
####### GLOBALS #########

# load todays input
HERE = Path(__file__)
DAY = HERE.stem[3:]
INPUT = HERE.parent / "input" / f"adventofcode.com_2023_day_{DAY}_input.txt"
if INPUT.exists():
    TEXT = INPUT.read_text()
else:
    INPUT = None
# convenient for passing working between parts 1 and 2, and relevant stuff to vizualations 
NS = SimpleNamespace()

# parse the input (usually)
def parse(line):
    """simple text parser"""
    a,b,*c = line.split()
    return a, int(b[:-1]), ' '.join(c)

@dataclass
class A:
    a : str
    b : int
    c : list

if INPUT:
    PARSED = [A(*parse(_)) for _ in TEXT.splitlines()]
    MAP = Map(TEXT.splitlines())
    MAP.show()
    breakpoint()

# Visualize a 2D map
# import numpy as np
# np.set_printoptions(threshold=np.inf)
# ARRAY = np.zeros((z,y,x), dtype="uint8") # 3D Array
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
# nd.draw_networkx(G) # show network
# plt.show() # draw

######## Part 1 ##########
def p1(expect=0 if not USING_EXAMPLE else 0):
    breakpoint()
    return 0

######## Part 2 ##########
def p2(expect=0 if not USING_EXAMPLE else 0):
    return 0

##########################
if __name__ == "__main__":
    show(p1, p2)
