def goal_test(state, goal=None): #have we solved the puzzle?
    if goal is None:
        x = max(max(state))
        y = [x for x in range(max(max(state)), 0, -1)]
        goal = [[]] * (len(state) - 1)
        goal.append(y)
    return state == goal

def generate_moves(state):
    children = []
    for peg_ind, inital_peg in enumerate(state):  #for each peg
        if len(inital_peg) != 0: #if the initial peg is not empty
            disk = inital_peg[-1] #-1 index gives the top disk
            for index, target_peg in enumerate(state): #for each peg
                if peg_ind != index: #as long as the pegs are not the same
                    new_puzzle = [peg.copy() for peg in state] #make a copy of the puzzle
                    new_puzzle[peg_ind].remove(disk)
                    new_puzzle[index].append(disk) #in the new puzzle perform the move
                    if len(target_peg) == 0 or target_peg[-1] > disk:
                        children.append(new_puzzle)
                        print(f"Safe move from {state} to {new_puzzle} generated.")
                    else:
                        print(f"Unsafe move {state} to {new_puzzle}, dead-end.")
    return children