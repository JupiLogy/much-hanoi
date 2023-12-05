def num_pegs(state):
    return(len(state))

def num_discs(state):
    return(max(max(state)))

def validate_state(state, godmode=False):
    if not godmode:
        for lis in state:
            if sorted(lis, reverse=True)!=lis:
                return False
    flatstate = [disc for peg in state for disc in peg]
    if not (set(range(1,num_discs(state)+1)) == set(flatstate)\
            and len(flatstate) == len(set(flatstate))):
        return False
    return True
