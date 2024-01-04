""" day x """
from pathlib import Path
from dataclasses import dataclass
import sympy
from itertools import combinations
from utils import show, Map, USING_EXAMPLE, NS, get_input_2023
####### GLOBALS #########

# load todays input
TEXT = get_input_2023(Path(__file__)).splitlines()

@dataclass
class Hail:
    "12, 31, 28 @ -1, -2, -1"
    x: int
    y: int
    z: int
    vx: int
    vy: int
    vz: int

    @property
    def posn(self):
        return self.x, self.y, self.z

    @property
    def velocity(self):
        return self.vx, self.vy, self.vz

    def when_is_x(self,x):
        return (x - self.x) / self.vx

    def __str__(self):
        return f"{self.x}, {self.y}, {self.z} @ {self.vx}, {self.vy}, {self.vz}"

PARSE = lambda txt: tuple(map(int,", ".join(txt.split("@")).split(", ")))

HAIL = [Hail(*PARSE(txt)) for txt in TEXT]

######## Part 1 ##########
def line(pt1, pt2):
    a = pt1[1] - pt2[1]
    b = pt2[0] - pt1[0]
    c = pt1[0]*pt2[1] - pt2[0]*pt1[1]
    return a, b, -c

def intersection(ln1, ln2):
    d  = ln1[0] * ln2[1] - ln1[1] * ln2[0]
    dx = ln1[2] * ln2[1] - ln1[1] * ln2[2]
    dy = ln1[0] * ln2[2] - ln1[2] * ln2[0]
    if d != 0:
        x = dx / d
        y = dy / d
        return x,y
    return False

PRINT = print
if USING_EXAMPLE:
    P1XYMIN = 7
    P1XYMAX = 27
else:
    P1XYMIN = 200000000000000
    P1XYMAX = 400000000000000
    print = lambda x: None

def intersects(h1, h2):
    print(f"Hailstone A: {h1}")
    print(f"Hailstone B: {h2}")
    i = intersection(
        line((h1.x, h1.y), (h1.x + h1.vx, h1.y + h1.vy)),
        line((h2.x, h2.y), (h2.x + h2.vx, h2.y + h2.vy)))
    if i is False:
        print("Hailstones' paths are parallel; they never intersect.\n")
        return 0
    ix, iy = i
    t_a = h1.when_is_x(ix)
    t_b = h2.when_is_x(ix)
    if t_a < 0 or t_b < 0: # already happened
        if t_a < 0 and t_b < 0:
            print(f"Hailstones' paths crossed in the past for both hailstones.\n")
        elif t_a < 0:
            print(f"Hailstones' paths crossed in the past for Hailstone A.\n")
        else:
            print(f"Hailstones' paths crossed in the past for Hailstone B.\n")
        return 0

    if P1XYMIN <= ix <= P1XYMAX and P1XYMIN <= iy <= P1XYMAX:
        print(f"Hailstones' paths will cross inside the test area (at x={ix:.3f}, y={iy:.3f}).\n")
        return 1
    print(f"Hailstones' paths will cross outside the test area (at x={ix:.3f}, y={iy:.3f}).\n")
    return 0


def p1(expect=24627 if not USING_EXAMPLE else 2):
    return sum(intersects(h1,h2) for h1,h2 in combinations(HAIL,2))

######## Part 2 ##########
def p2(expect=527310134398221 if not USING_EXAMPLE else 47):
    """throw a stone through the cloud to hit all the hailstones
    in my head thats lust a 4d intersection problem but I don't have the maths for that!

    Determine the sum of the rock's (x,y,z) coordinate at t=0, for a rock that will hit every hailstone
    in our input data. The rock has constant velocity and is not affected by collisions.
    """
    # define SymPy rock symbols - these are our unknowns representing:
    # initial rock location (xr, yr, zr)
    # rock velocity (vxr, vyr, vzr)
    xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr yr zr vxr vyr vzr")

    equations = [] # we assemble a set of equations that must be true
    for stone in HAIL[:4]: # we don't need ALL the stones to find a solution. We need just enough.
        x, y, z = stone.posn
        vx, vy, vz = stone.velocity
        equations.append(sympy.Eq((xr-x)*(vy-vyr), (yr-y)*(vx-vxr)))
        equations.append(sympy.Eq((yr-y)*(vz-vzr), (zr-z)*(vy-vyr)))

    solutions = sympy.solve(equations) # SymPy does the hard work
    if solutions:
        solution = solutions[0]
        print(solutions)
        return sum([solution[xr], solution[yr], solution[zr]])



##########################
if __name__ == "__main__":
    show(p1, p2)
