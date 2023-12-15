"""day 12"""
from pathlib import Path
from utils import show, Map, USING_EXAMPLE, NS, get_input_2023
####### GLOBALS #########

# load todays input
TEXT = get_input_2023(Path(__file__)).splitlines()
INVALID = 9999
######## Part 1 ##########

def recursive_count(txt, tgt):
    if "?" in txt:
        pos = txt.index("?")
        s = txt[:pos]
        e = txt[pos+1:]
        return recursive_count(s+"."+e,tgt) + recursive_count(s+"#"+e,tgt)
    return 1 if [len(_) for _ in txt.split(".") if _] == tgt else 0

def p1(expect=7379 if not USING_EXAMPLE else 21):
    acc = 0
    for line in TEXT:
        ptn, cnt = line.split()
        tgt = list(map(int,cnt.split(",")))
        acc += recursive_count2(ptn,tgt)
    return acc

######## Part 2 ##########
def recursive_count2(txt, tgt):
    #print(txt,tgt)
    # remove full matches
    groups = [_ for _ in txt.split(".") if _]
    for g,l in zip(groups,tgt):
        if "?" in g:
            break
        if g != "#"*l:
            return 0
    if "?" in txt:
        pos = txt.index("?")
        s = txt[:pos]
        e = txt[pos+1:]
        return recursive_count2(s+"."+e,tgt) + recursive_count2(s+"#"+e,tgt)
    return 1 if [len(_) for _ in txt.split(".") if _] == tgt else 0

from functools import cache

def p2(expect=7732028747925 if not USING_EXAMPLE else 102050):
    acc = 0
    for n,line in enumerate(TEXT):
        print(n,acc,line)
        ptn, cnt = line.split()
        tgt = list(map(int,cnt.split(",")))
        acc += recursive_count2(ptn*5,tgt*5)
    return acc

def p2cheat():
    from re import match
    return sum((g:=cache(lambda m,d: not d if not m else (m[0]!='#' and g(m[1:],d))+(d and match(r'[#?]{%d}[.?]'%d[0],m) and g(m[d[0]+1:],d[1:]) or 0)))('?'.join([s[0]]*5)+'.',(*map(int,s[1].split(',')),)*5) for s in map(str.split,TEXT))

##########################
if __name__ == "__main__":
    show(p1, p2)
