""" day x """
from pathlib import Path
from dataclasses import dataclass
# import numpy as np
# import networkx as nx
# from nx.algorithms.shortest_paths.astar import astar_path_length
# import nx.drawing.nx_pylab as nd
# import matplotlib.pyplot as plt
# from collections import deque, Counter
# from itertools import combinations, permutations
# import re
# from functools import cache
from utils import show, Map, USING_EXAMPLE, NS, get_input_2023
####### GLOBALS #########

# load todays input
TEXT = get_input_2023(Path(__file__)).splitlines()

# parse the input
def parse_rules(line):
    """
    hdj{m>838:A,pv}
    """
    n, r = line[:-1].split("{") # remove rule brackets
    r = r.split(",")
    return n, r

def parse_parts(line):
    """
    {x=787,m=2655,a=1222,s=2876}
    """
    x,m,a,s = line[1:-1].split(",")
    return int(x[2:]), int(m[2:]), int(a[2:]), int(s[2:])

@dataclass
class Rule:
    """Input"""
    rules : list

    def process(self,x,m,a,s):
        for rule in self.rules:
            if rule in "RA":
                return rule
            if ":" in rule:
                # evaluate a condition
                cond,res = rule.split(":")
                if eval(cond):
                    if res in "RA":
                        return res
                    return RULES[res].process(x,m,a,s)
            else:
                # plain rule
                return RULES[rule].process(x,m,a,s)
        breakpoint()
        raise RuntimeError("No more Rules!!")

    def combs(self,space):
        acc = []
        space = {"x":4000,"m":4000,"a":4000,"s":4000}
        scombs = lambda d: d["x"]*d["m"]*d["a"]*d["s"]
        for rule in self.rules:
            if rule in "RA":
                acc += scombs(space)
        return acc

@dataclass
class Part:
    """Input"""
    x : int
    m : int
    a : int
    s : int

BREAK = TEXT.index("")
RULES = {}
for R in TEXT[:BREAK]:
    NAME, RULE_LIST = parse_rules(R)
    RULES[NAME] = Rule(RULE_LIST)
PARTS = [Part(*parse_parts(line)) for line in TEXT[BREAK+1:]]

######## Part 1 ##########
def accept_or_reject(part):
    """."""
    print(part)
    return RULES["in"].process(part.x, part.m, part.a, part.s)

def p1(expect=399284 if not USING_EXAMPLE else 19114):
    accepted = []
    for part in PARTS:
        if accept_or_reject(part) == "A":
            accepted.append(part)
    return sum(p.x+p.m+p.a+p.s for p in accepted)

######## Part 2 ##########
def p2(expect=0 if not USING_EXAMPLE else 0):
    return RULES["in"].combs()

##########################
if __name__ == "__main__":
    show(p1, p2)
