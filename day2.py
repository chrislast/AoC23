# import our helpers
from utils import show, Map, USING_EXAMPLE, get_input_2023
from pathlib import Path
####### GLOBALS #########

# load todays input
TEXT = get_input_2023(Path(__file__))

######## Part 1 ##########

def valid_game(turns):
    # max ball count
    R,G,B = (12, 13, 14)
    for turn in turns.split(";"):
        for balls in turn.split(","):
            balls = balls.strip()
            count, color = balls.split(" ")
            if color == "red" and int(count) > R:
                return False
            if color == "green" and int(count) > G:
                return False
            if color == "blue" and int(count) > B:
                return False
    return True

def p1(expect=0 if USING_EXAMPLE else 2476):
    acc = 0
    for line in TEXT.splitlines():
        _, game, *turns = line.split()
        gnum = int(game[:-1])
        turns = ' '.join(turns)
        if valid_game(turns):
            acc += gnum
    return acc

######## Part 2 ##########
def minimum_balls_needed_product(turns):
    R,G,B = (0, 0, 0)
    for turn in turns.split(";"):
        for ball in turn.split(","):
            count, color = ball.strip().split(" ")
            if color == "red":
                R=max(R,int(count))
            elif color == "green":
                G=max(G,int(count))
            elif color == "blue":
                B=max(B,int(count))
    return R*G*B

def p2(expect=0 if USING_EXAMPLE else 54911):
    acc = 0
    for line in TEXT.splitlines():
        _,_,*game = line.split()
        turns = ' '.join(game)
        acc += minimum_balls_needed_product(turns)
    return acc

if __name__ == "__main__":
    show(p1, p2)
