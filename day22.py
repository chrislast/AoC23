""" day 22

nice to get gold star on the day considering how long part 1
took.

last year it was 2d tetris, this year 3d tetris (with simple shapes)
build a 9x9x256 tower and let all the "bricks" fall to their
gravity position then see what you could remove

kept each "brick" as an independent object and used 3d-arrays and
copies of those arrays as playgrounds for the "bricks"

thankfully my part 1 solution made part 2 quite easy and I could
just add the extra data capture in to the 16 second runtime of part 1
for zero cost and add them up in part2

a minecraft visualization would be nice but not available on
debian OS bookworm for RPi5 yet
"""
from pathlib import Path
from dataclasses import dataclass
from functools import cached_property
import numpy as np
from utils import show, USING_EXAMPLE, get_input_2023
####### GLOBALS #########

# load todays input
TEXT = get_input_2023(Path(__file__)).splitlines()

# parse the input (usually)
def parse(line):
    """
    4,3,149~7,3,149
    """
    bmin, bmax = line.split("~")
    x,y,z = map(int,bmin.split(","))
    a,b,c = map(int,bmax.split(","))
    return  x, y, z, a-x+1, b-y+1, c-z+1

@dataclass
class Brick:
    """Input"""
    id : int
    x: int
    y: int
    z: int
    lenx: int
    leny: int
    lenz: int
    drop_count: int = 0

    @property
    def npslice(self):
        return (self.z, self.z+self.lenz,
                self.y, self.y+self.leny,
                self.x, self.x+self.lenx)

    @cached_property
    def npbrick(self):
        return np.full(
            (self.lenz,self.leny,self.lenx),
            self.id, dtype="uint16")

    @cached_property
    def empty_z_slice(self):
        return np.zeros((1,self.leny,self.lenx), dtype="uint16")

    @cached_property
    def full_z_slice(self):
        return np.full((1,self.leny,self.lenx), self.id, dtype="uint16")

    def drop(self,arr):
        while True:
            if self.z == 0:
                break
            if arr[self.z-1,self.y:self.y+self.leny,self.x:self.x+self.lenx].any():
                break
            z,zz,y,yy,x,xx = self.npslice
            arr[z-1,y:yy,x:xx] = self.full_z_slice
            arr[zz-1,y:yy,x:xx] = self.empty_z_slice
            self.z -= 1

    def set(self, arr, val):
        z,zz,y,yy,x,xx = self.npslice
        arr[z:zz,y:yy,x:xx] = val

BRICKS = {i+1:Brick(i+1,*parse(_)) for i,_ in enumerate(TEXT)}

XMAX = max(_.x+_.lenx-1 for _ in BRICKS.values())
YMAX = max(_.y+_.leny-1 for _ in BRICKS.values())
ZMAX = max(_.z+_.lenz-1 for _ in BRICKS.values())
ARRAY = np.zeros((ZMAX+1,YMAX+1,XMAX+1), dtype="uint16") # 3D Array

for BRICK in BRICKS.values():
    Z,ZZ,Y,YY,X,XX = BRICK.npslice
    ARRAY[Z:ZZ,Y:YY,X:XX] = BRICK.npbrick

######## Part 1 ##########
def drop(arr):
    """."""
    for i in range(ZMAX+1):
        for brick in set(arr[i].flat):
            if brick == 0:
                continue
            BRICKS[brick].drop(arr)

def p1(expect=428 if not USING_EXAMPLE else 5): # < 429
    a = ARRAY.copy()
    drop(a)
    for brick in BRICKS.values():
        brick.az = brick.z
    acc = 0
    for brick in BRICKS.values():
        b = a.copy()
        brick.set(b,0) # delete brick
        drop(b)
        brick.set(b,brick.id) # restore brick
        if np.array_equal(a,b):
            acc += 1
        for b in BRICKS.values(): # restore brick positions
            if b.z != b.az:
                b.z = b.az
                brick.drop_count += 1
    return acc

######## Part 2 ##########
def p2(expect=35654 if not USING_EXAMPLE else 7):
    return sum(brick.drop_count for brick in BRICKS.values())

##########################
if __name__ == "__main__":
    show(p1, p2)
