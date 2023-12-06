from utils.state_properties import *
from termcolor import colored as clr

def print_numbers_state(state):
    height = max([len(peglist) for peglist in state])
    numpegs = num_pegs(state)
    print("  "+" ||  "*numpegs)
    for level in range(height-1,-1,-1):
        lv_str = ""
        for peg in range(numpegs):
            if len(state[peg]) < level+1:
                lv_str += "   ||"
            else:
                lv_str += "   "+clr(f"{state[peg][level]:2}", attrs=["reverse"])
        print(lv_str)
    print(" _"+"_||__"*numpegs+"\n")

def print_blocks_state(state):
    height = max([len(peglist) for peglist in state])
    numpegs = num_pegs(state)
    numdiscs = num_discs(state)
    try:
        assert numpegs * numdiscs < 120
    except:
        print("Too many discs, or too many pegs.")
        print("This puzzle is too wide and probably")
        print("won't display well :(")
        return
    print("  "+"|".center(numdiscs*2)*numpegs)
    for level in range(height-1,-1,-1):
        lv_str = "  "
        for peg in range(numpegs):
            if len(state[peg]) < level+1:
                lv_str += "|".center(numdiscs*2)
            else:
                lv_str += clr(f"{state[peg][level]}".center(state[peg][level]*2-1), attrs=["reverse"]).center(numdiscs*2+8)
        print(lv_str)
    print("  "+"|".center(numdiscs*2,"_")*numpegs)
