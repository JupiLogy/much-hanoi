from graph_traversal import goal_test

def __puzzle_to_tuple__(puzzle):
    return tuple(tuple(peg) for peg in puzzle)
    """'TypeError: unhashable type: 'list' was thrown because elements added
    to a set must be hashable (immutable). Tuples are hashable, so this function returns
    a tuple of tuples, which is hashable and can be added to the set"""

def __path_trace__(node, visited):  # store the path from the root node to the goal node
    current = node  # store input node as current
    path = []  # initialize path list
    path.append(current)  # add current to path
    if __puzzle_to_tuple__(current) in visited:  # while the parent of the current node is not None
        current = visited[__puzzle_to_tuple__(current)]  # set current to the parent of the current node
        path.append(current)  # add current to path
    return path  # return the path to the goal state

def bfs(root):
    open_list = []
    visited = {}

    open_list.append(root) #append root to open list
    visited[__puzzle_to_tuple__(root)] = None #add root to visited set, no parent

    while True:
        current_node = open_list.pop(0) #pop element 0 from open list
        print(f"Searching node: {current_node}")

        if goal_test(current_node) == True: #if we have reached the goal state
            path_to_solution = __path_trace__(current_node) #return the path to the goal state
            return path_to_solution

        children = generate_moves(current_node) #generate valid states/moves from current state

        for current_child in children:
            child_puzzle_tuple = __puzzle_to_tuple__(current_child)
            if child_puzzle_tuple not in visited:
                open_list.append(current_child)
                visited[child_puzzle_tuple] = __puzzle_to_tuple__(current_node)
