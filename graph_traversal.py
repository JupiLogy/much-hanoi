class Node:
    #node class, stores the state of the puzzle
    def __init__(self, state):
        self.state = state #contains the entire puzzle state
    
    def goal_test(self, goal=None): #have we solved the puzzle?
        return None

    def print_puzzle(self): #display the state of the puzzle at each step
        print(self.state) #print 'peg' array

    def generate_moves(self):
        children = []
        for peg_ind, inital_peg in enumerate(self.state):  #for each peg
            if len(inital_peg) != 0: #if the initial peg is not empty
                disk = inital_peg[-1] #-1 index gives the top disk
                for index, target_peg in enumerate(self.state): #for each peg
                    if peg_ind != index: #as long as the pegs are not the same
                        new_puzzle = [peg_ind.copy() for peg in self.state] #make a copy of the puzzle
                        new_puzzle[peg_ind].remove(disk)
                        new_puzzle[index].append(disk)
                        # in the new puzzle perform the move
                        if len(target_peg) == 0 or target_peg[-1] > disk:
                            children.append(new_puzzle)
                            print(f"Safe move from {self.state} to {new_puzzle} generated.") #generate safe state
                        else:
                            print(f"Unsafe move {self.state} to {new_puzzle} marked as dead-end.") #mark unsafe states and do not explore them further
        return children