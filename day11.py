"""
day 11

made a major mistake in creating network graph of 140*140 nodes
279*279 edges with weights and asking networkx to find shortest paths
it works... eventually! but, runtime is longer than the time it took to code this solution

Rapberry Pi5
  networkx:  6613.491 seconds
  plain old python: 170ms

using itertools.combinations made things a little easier
"""
from pathlib import Path
from itertools import combinations
import numpy as np
from utils import show, USING_EXAMPLE, get_input_2023

####### GLOBALS #########

# load todays input
TEXT = get_input_2023(Path(__file__)).splitlines()

# Load map to numpy
H = len(TEXT)
W = len(TEXT[0])
ARRAY = np.zeros((H,W), dtype="uint8")
for y, line in enumerate(TEXT):
    ARRAY[y,:] = bytearray(line, "ascii")

# Create a numbered galaxy map
GALAXIES = {}
GNUM = 0
for y in range(H):
    for x in range(W):
        if ARRAY[y,x] == ord("#"):
            GNUM += 1
            GALAXIES[GNUM] = (y,x)

# Identify all empty columns
EMPTY_COLS = set()
for c in range(W):
    if len(set(ARRAY[:,c])) == 1:
        EMPTY_COLS.add(c)

# Identify all empty rows
EMPTY_ROWS = set()
for r in range(H):
    if len(set(ARRAY[r,:])) == 1:
        EMPTY_ROWS.add(r)

######## Part 1 ##########
def dist_through_expanded_space(src,dst,expansion):
    """distance between two galaxies adjusted for space expansion"""
    dsty,dstx = GALAXIES[dst]
    srcy,srcx = GALAXIES[src]
    dist = abs(dstx-srcx) + abs(dsty-srcy)
    # increase distance for each empty row or column crossed
    for row in EMPTY_ROWS:
        if srcy<row<dsty or srcy>row>dsty:
            dist += expansion-1
    for col in EMPTY_COLS:
        if srcx<col<dstx or srcx>col>dstx:
            dist += expansion-1
    return dist

def p1(expect=10494813 if not USING_EXAMPLE else 374):
    """expanded space is twice as big"""
    acc = 0
    for src, dst in combinations(GALAXIES,2): # 101,025 unique combinations
        acc += dist_through_expanded_space(src,dst,2)
    return acc

######## Part 2 ##########
def p2(expect=840988812853 if not USING_EXAMPLE else 82000210):
    """expanded space is 1,000,000 times bigger"""
    acc = 0
    for src, dst in combinations(GALAXIES,2):
        acc += dist_through_expanded_space(src,dst,1000000)
    return acc

##########################
if __name__ == "__main__":
    show(p1, p2)
