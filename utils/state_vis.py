from utils.state_properties import *

def print_numbers_state(state):
    height = max([len(peglist) for peglist in state])
    numpegs = num_pegs(state)
    print("")
    for level in range(height-1,-1,-1):
        lv_str = ""
        for peg in range(numpegs):
            if len(state[peg]) < level+1:
                lv_str += "    |"
            else:
                lv_str += f"{state[peg][level]:5}"
        print(lv_str)
    print("  "+"__|__"*numpegs+"\n")