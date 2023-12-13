"""day 13
new - cached_property is interesting - basically a lazy evaluation
"""
from pathlib import Path
from functools import cached_property
import numpy as np
from utils import show, USING_EXAMPLE, get_input_2023
####### GLOBALS #########

# load todays input
TEXT = get_input_2023(Path(__file__)).splitlines()

class Map:
    def __init__(self):
        self.text = []
        self.p1 = None
        self.p2 = None

    @cached_property
    def H(self):
        return len(self.text)

    @cached_property
    def W(self):
        return len(self.text[0])

    @cached_property
    def array(self):
        arr = np.zeros((self.H,self.W), dtype="uint8")
        for y, line in enumerate(self.text):
            arr[y,:] = bytearray(line, "ascii")
        return arr

# Load all the maps into iterable list of Map objects
MAPS = [Map()]
for LINE in TEXT:
    if LINE == "":
        MAPS.append(Map())
    else:
        MAPS[-1].text.append(LINE)

ASH = ord(".")
ROCK = ord("#")

######## Part 1 ##########
def is_col_mirror(m,col):
    """Can map be reflected at this column?"""
    cols = min(col+1,m.W-col-1)
    lhs = m.array[:,col-cols+1:col+1]
    rhs = m.array[:,col+1:col+cols+1]
    assert lhs.shape == rhs.shape
    rhs = np.fliplr(rhs)
    res = np.array_equal(lhs,rhs)
    return res

def is_row_mirror(m,row):
    """Can map be reflected at this row?"""
    rows = min(row+1,m.H-row-1)
    top = m.array[row-rows+1:row+1,:]
    bottom = m.array[row+1:row+rows+1,:]
    assert top.shape == bottom.shape
    bottom = np.flipud(bottom)
    res = np.array_equal(top,bottom)
    return res

def get_reflection_score(m):
    """return score for reflection
    when used for part2 we ignore part1 reflections
    """
    for col in range(m.W-1):
        score = col + 1
        if score != m.p1 and is_col_mirror(m,col):
            return score
    for row in range(m.H-1):
        score = (row + 1) * 100
        if score != m.p1 and is_row_mirror(m,row):
            return score
    return 0 # no reflection found becomes possible in part 2

def p1(expect=34918 if not USING_EXAMPLE else 405):
    for m in MAPS:
        m.p1 = get_reflection_score(m)
    return sum(m.p1 for m in MAPS)

######## Part 2 ##########
def find_smudge_reflection(m):
    """
    find a new reflection after removing smudges by swapping ROCK and ASH at
    each point and rechecking for a new reflection
    """
    for x in range(m.W):
        for y in range(m.H):
            # test each point with "smudge removed" (swap ROCK for ASH)
            smudge = m.array[y,x]
            m.array[y,x] = ASH if smudge == ROCK else ASH
            res = get_reflection_score(m)
            m.array[y,x] = smudge # unsmudge
            if res:
                return res

def p2(expect=33054 if not USING_EXAMPLE else 400):
    for m in MAPS:
        m.p2 = find_smudge_reflection(m)
    return sum(m.p2 for m in MAPS)

##########################
if __name__ == "__main__":
    show(p1, p2)
