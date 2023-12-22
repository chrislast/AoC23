""" day 20
part 1 - solved as directed brute force logic stepwise emulation

part 2 - stuck
Used graphviz to visualize logic circuit at reddit suggestion
edited input to make graphviz work
cat input/adventofcode.com_2023_day_20_input.viz | dot -Tsvg -o output/day20.png
gimp output/day20.png

shows flip flop chain counts down to fire 1 every nth circuit for 4 chains
final AND gate needs all set so answer is lcm of period of each chain

not happy with non-programming step to discover logic circuit but it was
educational
"""

from pathlib import Path
from dataclasses import dataclass, field
from collections import deque
import math
from utils import show, USING_EXAMPLE, get_input_2023

####### GLOBALS #########

# load todays input
TEXT = get_input_2023(Path(__file__)).splitlines()

# parse the input
FLIPFLOPS = []
CONJUNCTIONS = []
def parse(line):
    """
    broadcaster -> a
    %a -> inv, con
    &inv -> b
    %b -> con
    &con -> output
    """
    src,tgts = line.split(" -> ")
    tgts = tgts.split(", ")
    if src[0] == "%":
        flipflop = FlipFlop(src[1:],tgts)
        FLIPFLOPS.append(flipflop)
        return flipflop
    if src[0] == "&":
        con = Conjunction(src[1:],tgts)
        CONJUNCTIONS.append(con)
        return con
    return Broadcaster("broadcaster", tgts)

class Complete(StopIteration):
    """"""

@dataclass
class Module:
    name: str
    dests: list
    rx: list = field(default_factory=list) # list of input modules and pulse values e.g. [("bob",1),("jim",0)]

    def process(self):
        return ()

    def __lt__(self,obj):
        return self.name < obj.name

class Rx(Module):
    def process(self):
        for src,val in self.rx:
            if val == 0:
                raise Complete("done!")
            #print((src,val),end="")
        self.rx.clear()
        return ()

@dataclass
class FlipFlop(Module):
    """Input"""
    state: int = 0

    def process(self):
        pulse = self.rx[0][1]
        self.rx = self.rx[1:]
        if pulse:
            return ()
        self.state = 1 - self.state
        return ((dst,self.state) for dst in self.dests)

@dataclass
class Conjunction(Module):
    input_state: dict = field(default_factory=dict)

    def process(self):
        for src,pulse in self.rx:
            self.input_state[src] = pulse
        self.rx.clear()
        val = self.val()
        return ((dst,val) for dst in self.dests)

    def val(self):
        return 1-int(all(self.input_state.values()))


@dataclass
class Broadcaster(Module):
    def process(self):
        for _,pulse in self.rx:
            val = pulse
        self.rx.clear()
        return ((dst,val) for dst in self.dests)

@dataclass
class Button(Module):
    def process(self):
        return (("broadcaster",0),)

MODULES = {"output": Module("output",[]),
           "rx": Rx("rx",[])}
for LINE in TEXT:
    MODULE = parse(LINE)
    MODULES[MODULE.name] = MODULE

# update inputs for conjuction modules
for MODULE_NAME, MODULE in MODULES.items():
    for DEST in MODULE.dests:
        if isinstance(MODULES[DEST],Conjunction):
            MODULES[DEST].input_state[MODULE_NAME]=0

######## Part 1 ##########
def push_button(hi,lo):
    """."""
    button = Button("button",["broadcaster"])
    pulse_queue = deque([button])
    while pulse_queue:
        mod = pulse_queue.popleft()
        sigs = mod.process()
        for dst,val in sigs:
            if val:
                hi += 1
            else:
                lo += 1
            #print(f"{mod.name} -{HILO[val]}-> {dst}") # broadcaster -low-> a
            MODULES[dst].rx.append((mod.name, val))
            pulse_queue.append(MODULES[dst])
    return hi,lo

HILO = {0:"low",1:"high"}

def p1(expect=938065580 if not USING_EXAMPLE else [32000000,11687500]):
    hi = lo = 0
    for _ in range(1000):
        hi,lo = push_button(hi,lo)
    return hi*lo

######## Part 2 ##########
def p2(expect=250628960065793):
    # don't push any buttons just analyze logic chains
    modules = {}
    for line in TEXT:
        parts = line.split(' -> ')
        modules[parts[0]] = parts[1].split(', ')
    acc = []
    for m in modules['broadcaster']:
        m2 = m
        bintxt = ''
        while True:
            # decode chains of flip flops as bits in an integer
            g = modules['%'+m2]
            # flip-flops that link to a conjunction are ones
            # everything else is a zero
            bintxt = ('1' if len(g) == 2 or '%'+g[0] not in modules else '0') + bintxt
            nextl = [next_ for next_ in modules['%'+m2] if '%' + next_ in modules]
            if len(nextl) == 0:
                break
            m2 = nextl[0]
        #print(bintxt)
        acc += [int(bintxt, 2)]
    # find least common multiple of integers
    #print(acc)
    return math.lcm(*acc)

##########################
if __name__ == "__main__":
    show(p1, p2)
