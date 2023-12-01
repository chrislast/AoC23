# import our helpers
from types import SimpleNamespace
from utils import load, show, day, TRACE, Map, Path, USING_EXAMPLE
import visualizations as viz
import numpy as np

####### GLOBALS #########

# load todays input data as a docstring
TEXT = load(day(__file__)).splitlines()
# convenient for passing working between parts 1 and 2, and relevant stuff to vizualations 
NS = SimpleNamespace()

# parse the input
def parse(line):
    a,b,*c = line.split()
    return a, int(b), c

# PARSED = [parse(_) for _ in TEXT]

# np.set_printoptions(threshold=np.inf)
# ARRAY = np.zeros((z,y,x), dtype="uint8") # 3D Array
# ARRAY_SLICE = ARRAY[0:2,0:3,22:26] # 2 layers, 3 rows, 4 columns
# ARRAY_SLICE = ARRAY[0:2,:,22:26] # 2 layers, all rows, 4 columns
# Map(ARRAY).show() # draw

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
def p1(expect=0 if USING_EXAMPLE else 0):
    breakpoint()
    return 0

######## Part 2 ##########
def p2(expect=0 if USING_EXAMPLE else 0):
    return 0

if __name__ == "__main__":
    show(p1, p2)
    #viz.viz?(NS)
