class Search:
    # class to perform searching

    def puzzle_to_tuple(self, puzzle):
        return tuple(tuple(peg) for peg in puzzle)
        """'TypeError: unhashable type: 'list' was thrown because elements added
        to a set must be hashable (immutable). Tuples are hashable, so this function returns
        a tuple of tuples, which is hashable and can be added to the set"""

    def path_trace(self, node):  # store the path from the root node to the goal node
        current = node  # store input node as current
        path = []  # initialize path list
        path.append(current)  # add current to path
        while current.parent != None:  # while the parent of the current node is not None
            current = current.parent  # set current to the parent of the current node
            path.append(current)  # add current to path
        return path  # return the path to the goal state

    def bfs(self, root):
        open_list = []
        visited = {}

        open_list.append(root)
        visited.add(self.puzzle_to_tuple(root.puzzle))

    def a_star_search(self, root):
        open_list = [] #similar to DFS implentation, initialize open list and visited set
        visited = {}

        open_list.append(root) #append root to open list
        visited.add(self.puzzle_to_tuple(root.puzzle)) #add root to visited set
        #the puzzle_to_tuple function is called again to avoid hashable error

        while True:
            current_Node = open_list.pop(0) #pop element 0 from open list
            print(f"Searching node: {current_Node.puzzle}")

            if current_Node.goal_test() == True: #if we have reached the goal state
                path_to_solution = self.path_trace(current_Node) #return the path to the goal state
                return path_to_solution

            children = current_Node.generate_moves() #generate valid states/moves from current state

            for current_child in children:
                child_puzzle_tuple = self.puzzle_to_tuple(current_child.state)
                if child_puzzle_tuple not in visited:
                    open_list.append(current_child)
                    visited[child_puzzle_tuple] = self.puzzle_to_tuple(current_Node).add(child_puzzle_tuple)
 
            open_list.sort(key=lambda x: x.f) #anonymous function to sort open list by f value of states
