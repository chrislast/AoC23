"""day 15"""
from pathlib import Path
from utils import show, Map, USING_EXAMPLE, NS, get_input_2023

####### GLOBALS #########
# load todays input
TEXT = get_input_2023(Path(__file__)).splitlines()
TEXT = ''.join(TEXT)
TEXT = TEXT.split(",")

######## Part 1 ##########
def HASH(s):
    """
    1. Determine the ASCII code for the current character of the string.
    2. Increase the current value by the ASCII code you just determined.
    3. Set the current value to itself multiplied by 17.
    4. Set the current value to the remainder of dividing itself by 256."""
    acc = 0
    for c in s:
        acc += ord(c)
        acc *= 17
        acc &= 0xff
    return acc

def p1(expect=520500 if not USING_EXAMPLE else 1320):
    return sum(HASH(_) for _ in TEXT)

######## Part 2 ##########
def score(boxes):
    """Calculate score by rules"""
    total = 0
    for box_index, lenses in enumerate(boxes):
        total += sum(
            (box_index+1) * (lens_index+1) * lens_focal_length
            for lens_index, lens_focal_length
            in enumerate(lenses.values()))
    return total

def fill(boxes):
    """Process instructions"""
    for instructions in TEXT:
        instruction = instructions.split("=")

        # add or change the focal length of a lens in a box
        if len(instruction)==2:
            lens, focal_length = instruction
            box = HASH(lens)
            boxes[box][lens] = int(focal_length)

        # otherwise remove the lens from a box if it exists
        else:
            lens = instruction[0][:-1]
            box = HASH(lens)
            if lens in boxes[box]:
                boxes[box].pop(lens)

def p2(expect=213097 if not USING_EXAMPLE else 145):
    """python3 dictionaries are always ordered now making part 2 much easier
    by preserving add order and handling key removal transparently"""
    boxes = [{} for _ in range(256)] # get 256 empty "boxes"
    fill(boxes)
    return score(boxes)

##########################
if __name__ == "__main__":
    show(p1, p2)
