""" day x """
from pathlib import Path
from collections import deque
from functools import cache
import numpy as np
from utils import show, Map, USING_EXAMPLE, NS, get_input_2023
####### GLOBALS #########

# load todays input
TEXT = get_input_2023(Path(__file__)).splitlines()

H = len(TEXT)
W = len(TEXT[0])
MAP = np.zeros((H,W), dtype="uint8") # 2D Array
for Y, LINE in enumerate(TEXT):
    MAP[Y,:] = bytearray(LINE, "ascii")

EMPTY = ord(".")
LR90 = ord("/")
RL90 = ord("\\")
H180 = ord("-")
V180 = ord("|")

UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)

######## Part 1 ##########
@cache
def new_beams(dx,dy,thing):
    """caching this function saves 75% of total runtime"""
    if thing == EMPTY or (dx and thing==H180) or (dy and thing==V180):
        return ((dx,dy),)    # ignore
    if thing == H180:
        return (RIGHT,LEFT)  # split
    if thing == V180:
        return (UP,DOWN)     # split
    if thing == LR90:
        return ((-dy, -dx),) # bounce
    return ((dy, dx),)       # bounce

def shine(startx,starty,dirx,diry):
    """shine a beam into MAP from any position in dirx,diry direction"""
    energized = np.zeros((H,W), dtype="uint8")
    beams = deque()
    beams.append((startx,starty,dirx,diry))
    seen = set() # needs to remember x,y pos and direction of beam
    while beams:
        beam = beams.popleft()
        x,y,dx,dy = beam
        if 0<=x<W and 0<=y<H and beam not in seen:
            energized[y,x] = 1
            seen.add(beam)
        else:
            # beam left map or is part of a loop so drop it now
            continue
        for beam in new_beams(dx,dy,MAP[y,x]):
            dx,dy = beam
            beams.append((x+dx,y+dy,dx,dy))
    # return the total number of energized squares
    return sum(sum(energized))

def p1(expect=6906 if not USING_EXAMPLE else 46):
    """Find energized tiles when shining a light from top left"""
    return shine(0, 0, *RIGHT) # from top left, going right

######## Part 2 ##########
def p2(expect=7330 if not USING_EXAMPLE else 51):
    """Find maximum tiles energized when shining a light from all edge positions"""
    return max((
        max(shine(x,   0,   *DOWN)  for x in range(W)),  # top edge
        max(shine(x,   H-1, *UP)    for x in range(W)),  # bottom edge
        max(shine(0,   y,   *RIGHT) for y in range(H)),  # left edge
        max(shine(W-1, y,   *LEFT)  for y in range(H)))) # right edge

##########################
if __name__ == "__main__":
    show(p1, p2)
