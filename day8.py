# import our helpers
from utils import show, Map, USING_EXAMPLE, NS, get_input_2023
from pathlib import Path
from math import lcm

####### GLOBALS #########

# load todays input
TEXT = get_input_2023(Path(__file__))

DIRECTIONS = TEXT.splitlines()[0]

def direction():
    """generator to loop through L and R instructions forever"""
    lr_to_index = {"L":0,"R":1}
    while True:
        for l_or_r in DIRECTIONS:
            yield lr_to_index[l_or_r]

# 0123456789012345
# RVN = (BXB, VJV)
# ^^^    ^^^  ^^^
MAP = {_[0:3]: (_[7:10],_[12:15]) for _ in TEXT.splitlines()[2:]}
# if we have been through each point more times than we have directions
UNREACHABLE = len(MAP)*len(DIRECTIONS)

######## Part 1 ##########
def get_steps(s,e):
    acc = 0
    node = s
    d = direction()
    while node != e:
        # part 2 needs to spot unreachable nodes
        if acc == UNREACHABLE:
            return None
        node = MAP[node][next(d)]
        acc += 1
    return acc

def p1(expect=22357 if not USING_EXAMPLE else 0):
    return get_steps("AAA","ZZZ")

#from collections import combinations
######## Part 2 ##########
def p2(expect=10371555451871 if not USING_EXAMPLE else 0):
    starts = [_ for _ in MAP if _[2]=="A"]
    ends = [_ for _ in MAP if _[2]=="Z"]
    found = []
    for s in starts:
        for e in ends:
            steps = get_steps(s,e)
            if steps:
                found.append(steps)
    return lcm(*found)

##########################
if __name__ == "__main__":
    show(p1, p2)
