# import our helpers
from utils import show, USING_EXAMPLE, get_input_2023
from pathlib import Path
from dataclasses import dataclass
####### GLOBALS #########

# load todays input
TEXT = get_input_2023(Path(__file__))

# parse the input (usually)
def parse(line):
    """
    Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    """
    s1, s2 = line.split("|")
    s11,s12 = s1.split(":")
    n = int(s11.split()[1])
    c = list(map(int,s12.split()))
    x = list(map(int,s2.split()))
    intersect = set(c)&set(x)
    if intersect:
        score = 1 << (len(intersect)-1)
    else:
        score=0
    wins = len(intersect)
    return n,c,x,score,wins

@dataclass
class A:
    n : int
    c : list
    x : list
    score: int 
    wins: int 

PARSED = [A(*parse(_)) for _ in TEXT.splitlines()]

######## Part 1 ##########
def p1(expect=23673 if not USING_EXAMPLE else 13):
    return sum([_.score for _ in PARSED])

######## Part 2 ##########
def p2(expect=12263631 if not USING_EXAMPLE else 30):
    acc = [1]*len(PARSED)
    for n,c  in enumerate(PARSED):
        w = c.wins
        for _ in range(w):
            acc[n+1+_] += acc[n]
    return sum(acc)

##########################
if __name__ == "__main__":
    show(p1, p2)
