from search import *
from graph_traversal import *

def main():
    print("Current puzzle state is:")
    print(root)
    print("Puzzle has "+str(num_pegs(root))+" pegs, and "+str(num_discs(root))+" discs.")
    if not validate_state(root):
        print("Puzzle state invalid. Please try again.")
        make_state()

def make_state():
    print("Making state.")

def make_custom_state():
    print("State guidelines:")
    print("1. There must not be duplicate discs. No two discs can be the same size.")
    print("2. ")

def state_search():
    print('Initial State of puzzle:')
    print(root)
    print("Ready to execute state search?")
    print("y = Yes")
    print("n = No or Modify puzzle shape")
    choice = input("(y/n): ")
    if choice == "y":
        print("Solving with BFS")
        solution_path = bfs(root)
        solution_path.reverse()  # Reverse the path to display the solution
        print("Path to solution:")
        for i, node in enumerate(solution_path):
            print(f"Step {i}")  # Print the step we are up to in the puzzle solution
            print(node)
    elif choice == "n":
        main()
    else:
        print("Invalid input")
        state_search()

# Initialize a basic puzzle
root = [[5, 4, 3, 2, 1], [], []]

main()
