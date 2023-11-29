#main function - creates UI for user to select which algorithm to use
def main():
    print('Initial State of puzzle:')
    root.print_puzzle()
    print("Which algorithm would you like to use to solve the Tower of Hanoi?")
    print("2. A* Search")
    print("3. Exit")
    choice = input("Please enter 2 or 3: ")
    if choice == "2":
        print("Solving with A* Search")
        search = Search()
        solution_path = search.a_star_search(root)
        # Display the action plan for DFS
        solution_path.reverse()  # Reverse the path to display the solution
        print("Path to solution:")
        for i, node in enumerate(solution_path):
            print(f"Step {i}")  # Print the step we are up to in the puzzle solution
            node.print_puzzle()
    elif choice == "3":
        print("Exiting...")
        exit()
    else:
        print("Invalid input, please enter 2 or 3")
        main()


# Initialize the puzzle, and display minimum number of steps to solve
initial_state = [5, 4, 3, 2, 1], [], []
root = Node(*initial_state)
print(root.steps())

# Call main function
main()
