# import our helpers
from utils import show, Map, USING_EXAMPLE, NS, get_input_2023
from pathlib import Path
from dataclasses import dataclass
from collections import Counter
####### GLOBALS #########

# load todays input
TEXT = get_input_2023(Path(__file__))

# parse the input (usually)
def parse(line):
    """
    fmt
    """
    a,b = line.split()
    return a, int(b)

@dataclass
class CamelPokerHand:
    hand : str
    bid : int

    def __lt__(self,obj):
        if self.score < obj.score:
            return True
        if self.score > obj.score:
            return False
        return self.rank < obj.rank

    def _score(self, counts):
        if counts[0] == 5:
            return 6
        if counts[0] == 4:
            return 5
        if counts[0] == 3 and counts[1] == 2:
            return 4
        if counts[0] == 3:
            return 3
        if counts[0] == 2 and counts[1] == 2:
            return 2
        if counts[0] == 2:
            return 1
        return 0

    def score1(self):
        c = Counter(self.hand)
        counts = sorted(c.values(),reverse=True)
        return self._score(counts)

    def score2(self):
        """J means Joker so use as most prevalent card"""
        c = Counter(self.hand)
        jokers = c["J"]
        c["J"] = 0
        counts = sorted(c.values(),reverse=True)
        counts[0] += jokers
        return self._score(counts)

    def rank1(self):
        return ['23456789TJQKA'.index(_) for _ in self.hand]

    def rank2(self):
        """Joker counts as lowest"""
        return ['J23456789TQKA'.index(_) for _ in self.hand]

# Rank and score all hands according to rules
HANDS = [CamelPokerHand(*parse(_)) for _ in TEXT.splitlines()]

######## Part 1 ##########
def score():
    acc = 0
    for n, hand in enumerate(sorted(HANDS)):
        acc += (1+n)*hand.bid
    return acc

def p1(expect=251806792 if not USING_EXAMPLE else 6440):
    for _ in HANDS:
        _.score = _.score1()
        _.rank = _.rank1()
    return score()

######## Part 2 ##########
def p2(expect=252113488 if not USING_EXAMPLE else 5905):
    for _ in HANDS:
        _.score = _.score2()
        _.rank = _.rank2()
    return score()

##########################
if __name__ == "__main__":
    show(p1, p2)
