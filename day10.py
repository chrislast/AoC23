"""day 10"""
from pathlib import Path
import numpy as np
from collections import deque
from utils import show, Map, USING_EXAMPLE, get_input_2023
####### GLOBALS #########

# load todays input
TEXT = get_input_2023(Path(__file__)).strip().splitlines()

# Problem is a 2D rectangular map
H = len(TEXT)
W = len(TEXT[0])

# Map used for Part 1
A = np.zeros((H,W), dtype="uint8") # 2D Array
for Y, line in enumerate(TEXT):
    A[Y,:] = bytearray(line, "ascii")

# Map used for Part 2 - filled during part 1
B = np.zeros((H,W), dtype="uint8") # 2D Array

# Start position
START = np.where(A==ord("S"))
STARTYX = list(zip(START[0],START[1]))[0]

# Map data symbols
SE = ord("F")
NW = ord("J")
NS = ord("|")
NE = ord("L")
EW = ord("-")
SW = ord("7")
EMPTY = 0
LEFT = 1
RIGHT = 2

# Translate a map symbol to the (dy,dx) offsets of it's two exit points
NEXT_YX_OFFSET = {
    SE: ((1,0),(0,1)),
    NW: ((-1,0),(0,-1)),
    NS: ((-1,0),(1,0)),
    NE: ((-1,0),(0,1)),
    EW: ((0,1),(0,-1)),
    SW: ((1,0),(0,-1))}

######## Part 1 ##########
def start_pipe_shape():
    """return pipe shape to replace S"""
    y,x = STARTYX
    # start with all pipes
    shapes = set([SE,NW,NS,NE,EW,SW])
    # keep connecting pipes that connect to neighbours
    if A[y-1,x] in (SE,NS,SW):    # if north neighbour points south
        shapes &= set([NW,NS,NE]) # keep north-going pipes
    if A[y+1,x] in (NE,NS,NW):    # etc.
        shapes &= set([SW,NS,SE])
    if A[y,x-1] in (NE,EW,SE):
        shapes &= set([NW,EW,SW])
    if A[y,x+1] in (NW,EW,SW):
        shapes &= set([NE,EW,SE])
    assert len(shapes) == 1
    return shapes.pop()

def get_steps_in_pipe_loop():
    """return total number of steps to traverse pipe loop"""
    y,x = STARTYX
    curr = start_pipe_shape()
    steps = 0
    seen = set()
    while True:
        steps += 1
        # Add the pipe part to the empty map for part 2
        B[y,x] = curr
        # track where we have been (including start)
        seen.add((y,x))
        # move somewhere we haven't been
        dy,dx = NEXT_YX_OFFSET[curr][0]
        if (y+dy, x+dx) in seen:
            dy,dx = NEXT_YX_OFFSET[curr][1]
        y, x = y+dy, x+dx
        curr = A[y,x]
        # completed loop
        if (y,x) == STARTYX:
            return steps

def p1(expect=6768 if not USING_EXAMPLE else 0):
    """return number of steps to get furthest from start"""
    steps = get_steps_in_pipe_loop()
    return steps//2


######## Part 2 ##########
def fill_if_empty(y,x,val):
    """if index is valid and content is empty, set it to val"""
    if (0 <= y < H) and (0 <= x < W) and (B[y,x] == EMPTY):
        B[y,x] = val
        return True
    return False

def add_left_and_right_borders():
    """Add left right borders to all pipe sides"""
    y,x = STARTYX
    seen = set()
    while True:
        curr = B[y,x]
        seen.add((y,x))
        dy,dx = NEXT_YX_OFFSET[curr][0]
        if (y+dy, x+dx) in seen:
            dy,dx = NEXT_YX_OFFSET[curr][1]
        y, x = y+dy, x+dx
        ncurr = B[y,x]
        if dy == -1: # going north
            fill_if_empty(y,x-1,LEFT)
            fill_if_empty(y,x+1,RIGHT)
            if ncurr == SE: # turning right
                fill_if_empty(y+dy,x,LEFT) # ahead is LEFT
            elif ncurr == SW: # turning left
                fill_if_empty(y+dy,x,RIGHT) # ahead is RIGHT
        elif dy == 1: # going south
            fill_if_empty(y,x-1,RIGHT)
            fill_if_empty(y,x+1,LEFT)
            if ncurr == NW: # turning right
                fill_if_empty(y+dy,x,LEFT) # ahead is LEFT
            elif ncurr == NE: # turning left
                fill_if_empty(y+dy,x,RIGHT) # ahead is RIGHT
        elif dx == 1: # going east
            fill_if_empty(y-1,x,LEFT)
            fill_if_empty(y+1,x,RIGHT)
            if ncurr == SW: # turning right
                fill_if_empty(y,x+dx,LEFT) # ahead is LEFT
            elif ncurr == NW: # turning left
                fill_if_empty(y,x+dx,RIGHT) # ahead is RIGHT
        else: # going west
            fill_if_empty(y-1,x,RIGHT)
            fill_if_empty(y+1,x,LEFT)
            if ncurr == NE: # turning right
                fill_if_empty(y,x+dx,LEFT) # ahead is LEFT
            elif ncurr == SE: # turning left
                fill_if_empty(y,x+dx,RIGHT) # ahead is RIGHT
        if (y,x) == STARTYX:
            return

def flood_fill_empty(value):
    """flood fill EMPTY points adjacent to VALUE with VALUE"""
    found = np.where(B==value)
    yx = deque(zip(found[0],found[1]))
    while yx:
        y, x = yx.popleft()
        for neigh in [(y-1,x),(y+1,x),(y,x-1),(y,x+1)]:
            if fill_if_empty(*neigh,value):
                yx.append(neigh)

def p2(expect=351 if not USING_EXAMPLE else [4,8,10]):
    """B was created in part 1"""
    add_left_and_right_borders()
    flood_fill_empty(LEFT)
    flood_fill_empty(RIGHT)
    if not USING_EXAMPLE:
        Map(B).save("output/10.png")
    if RIGHT in B[0,:]: # assumes not all first row is pipe
        return len(np.where(B==LEFT)[0])
    return len(np.where(B==RIGHT)[0])

##########################
if __name__ == "__main__":
    show(p1, p2)
