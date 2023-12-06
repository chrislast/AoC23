# import our helpers
from utils import show, Map, USING_EXAMPLE, NS, get_input_2023
from pathlib import Path
from dataclasses import dataclass
import math
####### GLOBALS #########

# load todays input
TEXT = get_input_2023(Path(__file__)).splitlines()

# Time:      7  15   30
# Distance:  9  40  200

Tp1 = list(map(int,TEXT[0].split()[1:]))
Dp1 = list(map(int,TEXT[1].split()[1:]))
Tp2 = int(TEXT[0].replace(" ","").split(":")[1])
Dp2 = int(TEXT[1].replace(" ","").split(":")[1])

def wins(pressed,racelen,record):
    moving = racelen - pressed
    distance = moving * pressed
    if distance > record:
        res = moving*pressed
    else:
        res = 0
    return res

######## Part 1 ##########
def p1(expect=114400 if not USING_EXAMPLE else 288):
    a = []
    for t,d in zip(Tp1,Dp1):
        acc = 0
        for pressed in range(t):
            if wins(pressed,t,d):
                acc += 1 
        a.append(acc)
    return math.prod(a)

######## Part 2 ##########
def lowest_winner():
    # use binary search to find lower bound
    # i'm sure there's a library for this...
    guess = Tp2//2
    inc = Tp2//4
    while True:
        lo = wins(guess,Tp2,Dp2)
        hi = wins(guess+1,Tp2,Dp2)
        if hi and not lo:
            return guess + 1
        if lo:
            guess -= max(1,inc)
        else:
            guess += max(1,inc)
        inc //= 2

def highest_winner():
    # use binary search to find upper bound
    guess = Tp2//2
    inc = Tp2//4
    while True:
        lo = wins(guess,Tp2,Dp2)
        hi = wins(guess+1,Tp2,Dp2)
        if lo and not hi:
            return guess
        if lo:
            guess += max(1,inc)
        else:
            guess -= max(1,inc)
        inc //= 2

def p2(expect=21039729 if not USING_EXAMPLE else 71503):
    return highest_winner() - lowest_winner() + 1

##########################
if __name__ == "__main__":
    show(p1, p2)
