# import our helpers
from utils import show, Map, USING_EXAMPLE, NS, get_input_2023
from pathlib import Path
from dataclasses import dataclass
####### GLOBALS #########

# load todays input
TEXT = get_input_2023(Path(__file__)).strip().splitlines()
SEEDS = list(map(int,TEXT[0].split()[1:]))

@dataclass
class Mapper:
    name: str
    rules: list

    def to_dst(self, n):
        for dst, src, rng in self.rules:
            if src <= n < src+rng:
                return dst + (n-src)
        return n

    def to_src(self, n):
        for dst, src, rng in self.rules:
            if dst <= n < dst+rng:
                return src + (n-dst)
        return n

# list of Mapper mapping objects
X2Y = []
for line in TEXT[2:]:
    if line.strip():
        if line.strip() in """
            seed-to-soil map:
            soil-to-fertilizer map:
            fertilizer-to-water map:
            water-to-light map:
            light-to-temperature map:
            temperature-to-humidity map:
            humidity-to-location map:
            """:
            key = Mapper(line.split()[0],[])
            X2Y.append(key)
        elif line:
            key.rules.append(list(map(int,line.split())))

def seed2location(seed):
    n = seed
    for transform in X2Y:
        n = transform.to_dst(n)
    #print(f"seed -> {seed} -> location {n}")
    return n


SEEDS2 = list(zip(SEEDS[::2],SEEDS[1::2]))
SEEDS2 = [(smin,smin+n) for smin,n in SEEDS2]
def is_seed(n):
    for smin, smax in SEEDS2:
        if smin <= n < smax:
            return True
    return False

def location2seed(loc):
    n = loc
    #print(f"location {loc}", end="")
    for transform in X2Y[::-1]:
        n = transform.to_src(n)
        #print(f" -> {n}", end="")
    #print("")
    return n

######## Part 1 ##########
def p1(expect=525792406 if not USING_EXAMPLE else 35):
    locs = [seed2location(seed) for seed in SEEDS]
    return min(locs)

######## Part 2 ##########
# 761 seconds brute force to check fom 1 to solution :(
# it turns out answer is one of range starts though
# so I'll check those first! pretty sure that won't be a general solution though
def p2(expect=79004094 if not USING_EXAMPLE else 46):
    BRUTE_FORCE = False
    if BRUTE_FORCE or USING_EXAMPLE:
        n = 0
        while True:
            if is_seed(location2seed(n)):
                return n
            n += 1
    #worksforme
    acc = []
    for dst in [_[0] for _ in X2Y[-1].rules]:
        if is_seed(location2seed(dst)):
            acc.append(dst)
    return min(acc)
    

##########################
if __name__ == "__main__":
    show(p1, p2)
