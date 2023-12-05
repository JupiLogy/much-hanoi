from search import *
from graph_traversal import *
from utils.state_properties import *
from utils.state_gen import *
from play import play

def main(state):
    print("Current starting state is:")
    print(state)
    try:
        print("Puzzle has "+str(num_pegs(state))+" pegs, and "+str(num_discs(state))+" discs.")
        assert validate_state(state)
    except:
        print("Puzzle state invalid. Please try again.")
        make_state(state)
    print("You may:")
    print(" - (c)hange starting state")
    print(" - (p)lay with this state")
    print(" - generate full (g)raph")
    print(" - (a)utomatically solve")
    choice = input("(c)hange/(p)lay/(g)raph/(a)utosolve: ")
    if choice == "c":
        make_state(state)
    elif choice == "p":
        play(state)
    elif choice == "g":
        generate_graph(state)
    elif choice == "a":
        autosolve(state)

def autosolve(state):
    print('Initial State of puzzle:')
    print(state)
    print("Ready to execute state search?")
    choice = input("(y)es/(m)enu: ")
    if choice == "y":
        print("Solving with BFS")
        solution_path = bfs(state)
        solution_path.reverse()  # Reverse the path to display the solution
        print("Path to solution:")
        for i, node in enumerate(solution_path):
            print(f"Step {i}")  # Print the step we are up to in the puzzle solution
            print(node)
    elif choice == "m":
        main()
    else:
        print("Invalid input")
        autosolve(state)

# Initialize a basic puzzle
main([[5, 4, 3, 2, 1], [], []])
