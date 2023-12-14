"""
day 14

1 - tilt a pattern with rolling rocks and score its final state
2 - roll the pattern in a circle until it starts to repeat
    find where the billionth state would fall in the loop
    and score that

Part 2 took 18s on RPi 5 so there is probably room for optimisation
swapped O(n2) loops for O(n) loop with array locate on tilt - 18s -> 12.7s
swapped O(n) loop of sorted lists of array locate on tilt - 12.7s -> ?
"""
from pathlib import Path
import numpy as np
from utils import show, USING_EXAMPLE, get_input_2023

####### GLOBALS #########
# load todays input
TEXT = get_input_2023(Path(__file__)).splitlines()

H = len(TEXT)
W = len(TEXT[0])
MAP = np.zeros((H,W), dtype="uint8")
for Y, LINE in enumerate(TEXT):
    MAP[Y,:] = bytearray(LINE, "ascii")

# Take a copy for part 2
MAP2 = MAP.copy()

ASH = ord(".")
ROCK = ord("#")
ROLL = ord("O")

######## Part 1 ##########
def load_on_north_wall(m):
    """return value of current rolling rock positions"""
    acc = 0
    rollers = np.where(m==ROLL)
    for y in rollers[0]:
        acc += H - y
    return acc

def roll_north(a,y,x):
    """roll a single round rock as far north as possible"""
    while y>0 and a[y-1,x] == ASH:
        a[y-1,x] = ROLL
        a[y,x] = ASH
        y -= 1


def tilt_north(m):
    """roll all round rocks north starting from top"""
    for y in range(H):
        for x in np.where(m[y]==ROLL)[0]:
            roll_north(m,y,x)

def p1(expect=105461 if not USING_EXAMPLE else 136):
    tilt_north(MAP)
    return load_on_north_wall(MAP)

######## Part 2 ##########
def roll_south(a,y,x):
    while y<(H-1) and a[y+1,x] == ASH:
        a[y+1,x] = ROLL
        a[y,x] = ASH
        y += 1
def roll_east(a,y,x):
    while x<(W-1) and a[y,x+1] == ASH:
        a[y,x+1] = ROLL
        a[y,x] = ASH
        x += 1
def roll_west(a,y,x):
    while x>0 and a[y,x-1] == ASH:
        a[y,x-1] = ROLL
        a[y,x] = ASH
        x -= 1

def tilt_south(m):
    for y in range(H-1,-1,-1):
        for x in np.where(m[y]==ROLL)[0]:
            roll_south(m,y,x)
def tilt_east(m):
    for x in range(W-1,-1,-1):
        for y in np.where(m[:,x]==ROLL)[0]:
            roll_east(m,y,x)
def tilt_west(m):
    for x in range(W):
        for y in np.where(m[:,x]==ROLL)[0]:
            roll_west(m,y,x)



def spin():
    """spin the platform once and return hash of its state"""
    tilt_north(MAP2)
    tilt_west(MAP2)
    tilt_south(MAP2)
    tilt_east(MAP2)
    return hash(bytes(MAP2))

def p2(expect=102829 if not USING_EXAMPLE else 64):
    """Spin the platform 1000000000 times"""
    h = hash(bytes(MAP2))
    target = 1000000000
    cache = []
    # keep spinning until we reach a state we've seen before
    while h not in cache:
        cache.append(h)
        h = spin()
    first = cache.index(h)
    # work out how often it repeats
    period = len(cache) - first
    # remove the settling steps before the main loop starts
    target -= first
    # remove all the unnecessary repeat loops
    target %= period
    # spin it to where it would have been at 1,000,000,000 spins
    for _ in range(target):
        spin()
    return load_on_north_wall(MAP2)

##########################
if __name__ == "__main__":
    show(p1, p2)
