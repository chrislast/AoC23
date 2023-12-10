""" day 9 """
from pathlib import Path
from utils import show, USING_EXAMPLE, get_input_2023

####### GLOBALS #########

# load todays input
TEXT = get_input_2023(Path(__file__))
PARSED = [list(map(int,_.split())) for _ in TEXT.splitlines()]
ALL_ZEROES = set([0])

######## Part 1 ##########
def recursive_diff(ints, part2=False):
    """
    recursively get rate of change of array items until
    and return the predicted next/prev value in tail recursion
    """
    if set(ints) == ALL_ZEROES:
        return 0 # first/last diff is also 0 on depth'th row

    # reduce all the integers to a list of their differences
    nextints = [ints[n+1]-ints[n] for n in range(len(ints)-1)]

    if part2:
        return ints[0] - recursive_diff(nextints, part2)
    return ints[-1] + recursive_diff(nextints)

def p1(x=1938731307 if not USING_EXAMPLE else 114):
    return sum(recursive_diff(row) for row in PARSED)

######## Part 2 ##########
def p2(x=948 if not USING_EXAMPLE else 2):
    return sum(recursive_diff(row, part2=True) for row in PARSED)

##########################
if __name__ == "__main__":
    show(p1, p2)
