from search import *
from graph_traversal import *
from utils.state_properties import *

def main(state):
    print("Current puzzle state is:")
    print(state)
    try:
        print("Puzzle has "+str(num_pegs(state))+" pegs, and "+str(num_discs(state))+" discs.")
        assert validate_state(state)
    except:
        print("Puzzle state invalid. Please try again.")
        make_state(state)

def make_state(state):
    while True:
        print("STATE CONFIGURATION")
        print("Would you like to start with a custom state,")
        print("or would you rather start from the default start state?")
        print("c = Custom state")
        print("d = Default state")
        print("m = Menu")
        choice = input("(c)ustom/(d)efault/(m)enu: ")
        if choice == "c":
            return make_custom_state(state)
        elif choice == "d":
            return make_default_state(state)
        elif choice == "m":
            if not validate_state(state):
                print("Puzzle state invalid. Please try again.")
            else: # State is valid, return to menu
                return state
        else:
            print("Unrecognised response.")

def make_default_state(state):
    while True:
        pegs = input("How many pegs? (Default 3)")
        discs = input("How many discs? (Default 5)")
        print("Creating puzzle with "+pegs+" pegs and "+discs+" discs.")
        choice = input("Okay? (y)es/(n)o/(m)enu: ")
        if choice == "y":
            return init_state_from_params(pegs, discs, state)
        elif choice == "n":
            pass
        elif choice == "m":
            return state
        else:
            print("Unrecognised response.")

def init_state_from_params(pegs, discs, state):
    # Only accepting state as arg in case pegs/discs don't validate.
    # Setting defaults if blank
    if pegs == "":
        pegs = 3
    if discs == "":
        discs = 5

    # Validating
    try:
        pegs = int(pegs)
        discs = int(discs)
        assert(pegs>2 and discs>0)
    except:
        print("Invalid number of pegs or discs.")
        print("Please ensure there are at least 3 pegs and 1 disc.")
        input("Press (enter) to return to the menu.")
        return make_default_state(state)

    # Generating
    state = [[] for i in range(pegs)]
    for i in range(len(pegs)):
        state[0][:0] = [i+1]
    return state

def make_custom_state(state):
    print("State guidelines:")
    print("1. There must not be duplicate discs. No two discs can be the same size.")
    print("2. The smallest disc must be \"1\". Each disc after that must increase")
    print("   in size by 1.")
    print("Example state: [[5, 4, 3, 2, 1], [], []]")
    print("Here, all discs are on the first peg.")
    print("There are 3 pegs and 5 discs.")
    print("The discs are in order.")
    while True:
        new_state = input("Your state: ")
        if validate_state(new_state, godmode=True):
            print("State validated!")
            print(new_state)
            return new_state
        else:
            print("State not valid.")
            choice = input("Try making custom state again? (y)es/(n)o")
            if choice == "y":
                pass
            elif choice == "n":
                return state
            else:
                print("Unrecognised response.")

def state_search():
    print('Initial State of puzzle:')
    print(root)
    print("Ready to execute state search?")
    choice = input("(y)es/(m)enu: ")
    if choice == "y":
        print("Solving with BFS")
        solution_path = bfs(root)
        solution_path.reverse()  # Reverse the path to display the solution
        print("Path to solution:")
        for i, node in enumerate(solution_path):
            print(f"Step {i}")  # Print the step we are up to in the puzzle solution
            print(node)
    elif choice == "m":
        main()
    else:
        print("Invalid input")
        state_search()

# Initialize a basic puzzle
main([[5, 4, 3, 2, 1], [], []])
