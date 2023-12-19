""" day 18 """
from pathlib import Path
from dataclasses import dataclass
import numpy as np
from collections import deque, Counter
from utils import show, Map, USING_EXAMPLE, NS, get_input_2023

####### GLOBALS #########

# load todays input
TEXT = get_input_2023(Path(__file__)).splitlines()

# parse the input (usually)
def parse(line):
    """
    U 2 (#caa173)
    """
    a,b,c = line.split()
    return a, int(b), int(c[2:-1],16)

@dataclass
class Dig:
    """Input"""
    dirn : chr
    dist : int
    color : int

INSTRUCTIONS = [Dig(*parse(_)) for _ in TEXT]

######## Part 1 ##########
def get_map(instructions):
    """."""
    minx=miny=maxx=maxy=x=y=0
    for i in instructions:
        if i.dirn == "U":
            y -= i.dist
            miny = min(miny,y)
        if i.dirn == "D":
            y += i.dist
            maxy = max(maxy,y)
        if i.dirn == "L":
            x -= i.dist
            minx = min(minx,x)
        if i.dirn == "R":
            x += i.dist
            maxx = max(maxx,x)
    assert x == y == 0
    H = maxy - miny + 3
    W = maxx - minx + 3

    x = -minx + 1
    y = -miny + 1
    MAP = np.zeros((H,W), dtype="uint8") # 2D Array

    for i in instructions:
        if i.dirn == "U":
            for _ in range(i.dist):
                y-=1
                MAP[y,x] = i.color!=0
        if i.dirn == "D":
            for _ in range(i.dist):
                y+=1
                MAP[y,x] = i.color!=0
        if i.dirn == "L":
            for _ in range(i.dist):
                x-=1
                MAP[y,x] = i.color!=0
        if i.dirn == "R":
            for _ in range(i.dist):
                x+=1
                MAP[y,x] = i.color!=0
    return MAP

EMPTY = 0xff

def flood(m):
    yx = deque(((0,0),))
    n = 0
    while yx:
        y, x = yx.popleft()
        n += 1
        H,W = m.shape
        if n>H*W:
            return
        for neigh in [(y-1,x),(y+1,x),(y,x-1),(y,x+1)]:
            y,x = neigh
            if 0<=y<H and 0<=x<W and m[y,x]==0:
                yx.append(neigh)
                m[y,x] = EMPTY

def p1(expect=52035 if not USING_EXAMPLE else 62):
    m = get_map(INSTRUCTIONS)
    H,W = m.shape
    #Map(m).show()
    flood(m)
    Map(m).show()
    empty = np.where(m==EMPTY)
    return H*W-len(empty[0])

######## Part 2 ##########

def newdig(d):
    dist,dirn = divmod(d.color,16)
    dirn = {0:"R",1:"D",2:"L",3:"U"}[dirn]
    return Dig(dirn,dist,1)

def calcxy(instructions):
    x=y=0
    pathlen = 0
    for i in instructions:
        i.x = x
        i.y = y
        if i.dirn == "R":
            x += i.dist
        elif i.dirn == "L":
            x -= i.dist
        elif i.dirn == "U":
            y -= i.dist
        else:
            y += i.dist
        pathlen += i.dist
    assert x==0 and y==0
    return pathlen/2 # half the path is outside shoelace area

def shoelace(instructions):
    #feed in the end of the loop first
    x,y = instructions[-1].x, instructions[-1].y
    area = 0
    for i in instructions:
        area += x*i.y - i.x*y
        x,y = i.x, i.y
    return area/2 # shoelace gives 2 * area


def p2(expect=60612092439765 if not USING_EXAMPLE else 952408144115):
    instructions = [newdig(_) for _ in INSTRUCTIONS]
    # Ho Ho Ho - Unable to allocate 1.28 TiB for an array with shape (1186331, 1186331)
    # m = get_map(i)
    plen = calcxy(instructions) # path length
    area = shoelace(instructions) # surrounded area
    return int(plen+area)+1 # +1 for 2 x corners

##########################
if __name__ == "__main__":
    show(p1, p2)
