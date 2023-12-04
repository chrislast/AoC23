# import our helpers
from utils import show, Map, USING_EXAMPLE, get_input_2023
from pathlib import Path
from dataclasses import dataclass
####### GLOBALS #########

# load todays input
TEXT = get_input_2023(Path(__file__))

SYMBOLS = set(TEXT) - set("0123456789.\n")
TEXT = TEXT.strip().splitlines()
SZ = len(TEXT)

# Visualize a 2D map
import numpy as np
np.set_printoptions(threshold=np.inf)
A = np.zeros((SZ,SZ), dtype="uint8") # 3D Array
for y, line in enumerate(TEXT):
    A[y,:] = bytearray(line,"ascii")
#Map(A).show()

def is_digit(c):
    return 0x30 <= c <= 0x39

def m(n):
    """keep array indices in bounds"""
    return min(max(n,0),SZ-1)


######## Part 1 ##########
def p1(expect=527369 if not USING_EXAMPLE else 4361):
    """
    find "numbers" with adjacent "symbols" and add them up
    """
    acc = 0
    # find all "numbers"
    for y in range(SZ): # 140 lines in input
        x=0
        while x<SZ: # 140 columns in input
            if is_digit(A[y,x]):
                # we found the start of a number
                start = x
                while x<(SZ-1) and is_digit(A[y,x+1]):
                    x+=1
                end = x
                # convert "number" to int
                n = int(bytearray(A[y,start:end+1]))
                # capture surrounding cells to a slice then handle as string
                t = bytearray(A[m(y-1):m(y+1)+1,m(start-1):m(end+1)+1]).decode("ascii")
                if set(t) & SYMBOLS:
                    # add number to running total if adajacent symbols are present
                    acc += n
            x += 1
    return acc

######## Part 2 ##########
def p2(expect=73074886 if not USING_EXAMPLE else 467835):
    """
    find all "gears"(*) with exactly two adjacent numbers
    and add up the product of their two numbers
    """
    # find all gears
    N = np.where(A==ord("*"))
    NXY = list(zip(N[0],N[1]))
    # store as a dict of y,x tuples with an intitially empty list of adjacent numbers
    acc = {k:[] for k in NXY}

    # find all numbers (like last time)
    for y in range(SZ):
        x=0
        while x<SZ:
            if is_digit(A[y,x]):
                start = x
                while x<(SZ-1) and is_digit(A[y,x+1]):
                    x+=1
                end = x
                # decode number to int (as before)
                n = int(bytearray(A[y,start:end+1]))
                # this time keep surroundings as array slice
                t = A[m(y-1):m(y+1)+1,m(start-1):m(end+1)+1]
                # find all gears in slice
                gears = np.where(t==ord("*"))
                gears = list(zip(gears[0],gears[1]))
                # for each adjacent gear
                for gy, gx in gears:
                    if y:         # else gy is already y value pf input
                        gy += y-1 # convert gy back to y value of input
                    if start:     # convert gx to input co-ords too
                        gx += start-1
                    # store the current number as adjacent to this gear
                    acc[(gy,gx)].append(n)
            x += 1
    two_tuples = [acc[_] for _ in acc if len(acc[_])==2]
    gear_ratios = [x*y for x,y in two_tuples]
    return sum(gear_ratios)

##########################
if __name__ == "__main__":
    show(p1, p2)
