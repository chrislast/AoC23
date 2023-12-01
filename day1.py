# import our helpers
from utils import load, show, day, TRACE, Map, Path, USING_EXAMPLE
from pathlib import Path

####### GLOBALS #########

# load todays input data as a docstring
TEXT = (Path(__file__).parent / "input" /
    "adventofcode.com_2023_day_1_input.txt").read_text()

DIGITS = {'one': '1', 'two': '2', 'three': '3', '1':'1', '2':'2', '3':'3',
          'four': '4', 'five': '5', 'six': '6', '4':'4', '5':'5','6':'6', 
          'seven': '7', 'eight': '8', 'nine': '9', '7':'7', '8':'8', '9':'9'}

######## Part 1 ##########
def first1(line):
    for char in line:
        if char in "123456789":
            return char

def last1(line):
    return first1(line[::-1])

def p1(expect=0 if USING_EXAMPLE else 55621):
    return sum([int(first1(_)+last1(_)) for _ in TEXT.split()])

######## Part 2 ##########
def first2(line):
    while line:
        for _ in DIGITS:
            if line.startswith(_):
                return DIGITS[_]
        line=line[1:]

def last2(line):
    pos = len(line)-1
    while pos>=0:
        for _ in DIGITS:
            if line[pos:].startswith(_):
                return DIGITS[_]
        pos-=1

def p2(expect=0 if USING_EXAMPLE else 53592):
    return sum([int(first2(_)+last2(_)) for _ in TEXT.split()])

if __name__ == "__main__":
    show(p1, p2)
