class Node:
    #node class, stores the state of the puzzle, as well as children and parent nodes
    def __init__(self, peg1, peg2, peg3):
        self.peg1 = peg1
        self.peg2 = peg2
        self.peg3 = peg3 #'pegs' are lists of integers, representing the disks on each peg
        self.parent = None 
        self.children = [] #states that can be reached from the current state
        self.puzzle = [self.peg1, self.peg2, self.peg3] #contains the entire puzzle state
        self.g = 0 #depth of the node
        self.f = self.get_f_value() #heuristic value of the node
    
    def create_child(self, peg1, peg2, peg3): #represent a new state reachable from the current state
        child = Node(peg1, peg2, peg3) #create a new node
        child.parent = self #parent of node is current node
        self.children.append(child) #add child to children list
        child.g = self.g + 1 #depth of child is depth of parent + 1
    
    def get_f_value(self): #calculate the heuristic value of the node
        h = len(self.peg3) #number of disks on peg 3
        #heuristic value is the number of disks on peg 3
        return h + self.g #f = g + h

    def goal_test(self): #have we solved the puzzle?
        goal_state = [5, 4, 3, 2, 1] #define the goal state
        return self.peg3 == goal_state and not self.peg1 and not self.peg2
        #if peg3 is arranged in ascending order with all disks we have reached the goal state

    def print_puzzle(self): #display the state of the puzzle at each step
        print('Peg1:', self.peg1)
        print('Peg2:', self.peg2)
        print('Peg3:', self.peg3) #print 'peg' array

    def generate_moves(self):
     if self.children == []: #only generate moves once ie. if the children list is empty
      for peg, inital_peg in enumerate(self.puzzle):  # for each peg
        if len(inital_peg) != 0:  # if the initial peg is not empty
            disk = inital_peg[-1]  # -1 index gives the top disk
            for index, target_peg in enumerate(self.puzzle):  # for each peg
                if peg != index:  # as long as the pegs are not the same
                    new_puzzle = [peg.copy() for peg in self.puzzle]  # make a copy of the puzzle
                    new_puzzle[peg].remove(disk)
                    new_puzzle[index].append(disk)
                    # in the new puzzle perform the move
                    if len(target_peg) == 0 or target_peg[-1] > disk:
                        self.create_child(*new_puzzle)  # form a new node from the new state if the move is safe
                        print(f"Safe move from {self.puzzle} to {new_puzzle} generated.") #generate safe state
                    else:
                        print(f"Unsafe move {self.puzzle} to {new_puzzle} marked as dead-end.") #mark unsafe states and do not explore them further
