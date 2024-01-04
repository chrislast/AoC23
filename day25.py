""" day 25 """
from pathlib import Path
from dataclasses import dataclass
# import numpy as np
import networkx as nx
# from nx.algorithms.shortest_paths.astar import astar_path_length
import networkx.drawing.nx_pylab as nd
import matplotlib.pyplot as plt
# from collections import deque, Counter
from itertools import combinations
# import re
# from functools import cache
from utils import show, Map, USING_EXAMPLE, NS, get_input_2023
####### GLOBALS #########

# load todays input
TEXT = get_input_2023(Path(__file__)).splitlines()

# parse the input
def parse(line):
    """
jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
    """
    s, d = line.split(": ")
    d = d.split(" ")
    return s,d

# Build a network graph
G = nx.Graph()
edges = 0
for txt in TEXT:
    src,dsts = parse(txt)
    G.add_node(src)
    for dst in dsts:
        if dst not in G:
            G.add_node(dst)
        G.add_edge(src,dst)
        edges += 1
print(f"{edges} edges -> {edges**3} combinations")

#nd.draw_networkx(G) # show network
#plt.show() # draw

######## Part 1 ##########
def fn():
    """."""

def p1(expect=0 if not USING_EXAMPLE else 0):
    explen = len(G.nodes)
    for edges in ((("shj","xhl"),("fxk","bcf"),("zgp","cgt")),) if not USING_EXAMPLE else combinations(G.edges, 3):
        g = G.copy()
        for edge in edges:
            g.remove_edge(*edge)
        rnode = list(g.nodes)[0]
        rlen = len(nx.descendants(g,rnode))+1
        if rlen < explen-3:
            break
    return rlen*(explen-rlen)

######## Part 2 ##########
def p2(expect=0 if not USING_EXAMPLE else 0):
    return 0

##########################
if __name__ == "__main__":
    show(p1, p2)
