from search import *
from graph_traversal import *

def main():
    print('Initial State of puzzle:')
    print(root)
    print("Which algorithm would you like to use to solve the Tower of Hanoi?")
    print("2. Breadth Search")
    print("3. Exit")
    choice = input("Please enter 2 or 3: ")
    if choice == "2":
        print("Solving with BFS")
        solution_path = bfs(root)
        solution_path.reverse()  # Reverse the path to display the solution
        print("Path to solution:")
        for i, node in enumerate(solution_path):
            print(f"Step {i}")  # Print the step we are up to in the puzzle solution
            print(node)
    elif choice == "3":
        print("Exiting...")
        exit()
    else:
        print("Invalid input, please enter 2 or 3")
        main()

# Initialize a basic puzzle
root = [[5, 4, 3, 2, 1], [], []]

main()
