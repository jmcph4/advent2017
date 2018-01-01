def taxicab_distance(a, b):
    """
    Returns the Manhattan distance of the given points
    """
    n = len(a)
    d = 0

    for i in range(n):
        d += abs(a[i] - b[i])

    return d

PERIOD = 2 # the period of the sequence

def sequ():
    """
    Generates the sequence corresponding to the number of steps to take at each
    turn when traversing memory
    """
    step = 0
    val = 1

    while True:
        if step == PERIOD:
            step = 0
            val += 1

        yield val
        step += 1

# movements
def right(pos):
    """
    Move right
    """
    return (pos[0]+1, pos[1])

def left(pos):
    """
    Move left
    """
    return (pos[0]-1, pos[1])

def up(pos):
    """
    Move up
    """
    return (pos[0], pos[1]+1)

def down(pos):
    """
    Move down
    """
    return (pos[0], pos[1]-1)

PORT_NUM = 1 # address of sole I/O port

def coordinates(n):
    """
    Returns the co-ordinates of the given address in memory
    """
    if n == PORT_NUM: # orient ourselves w.r.t. to I/O port
        return (0, 0)

    pos = (0, 0)
    seq = sequ()
    diff = n - 1
    
    while diff > 0:
        if diff == 0: # are we there yet?
            return pos

        # right branch
        branch_length = next(seq)
        for i in range(branch_length):
            if diff == 0: # are we there yet?
                return pos
            pos = right(pos)
            diff -= 1 # decrement difference

        # up branch
        branch_length = next(seq)
        for i in range(branch_length):
            if diff == 0: # are we there yet?
                return pos
            pos = up(pos)
            diff -= 1 # decrement difference

        # left branch
        branch_length = next(seq)
        for i in range(branch_length):
            if diff == 0: # are we there yet?
                return pos
            pos = left(pos)
            diff -= 1 # decrement difference

        # down branch
        branch_length = next(seq)
        for i in range(branch_length):
            if diff == 0: # are we there yet?
                return pos
            pos = down(pos)
            diff -= 1 # decrement difference
            
    return pos

def distance(n):
    """
    Returns the Manhattan distance from the I/O port to the given address
    """
    port_loc = coordinates(PORT_NUM)
    n_loc = coordinates(n)
    
    return taxicab_distance(port_loc, n_loc)

def num_steps(n):
    """
    Returns the number of steps required to get from the given address to the
    I/O port
    """
    if n == PORT_NUM:
        return 0

    pos = coordinates(n)
    
    return distance(n)

"""
# tests
print(num_steps(1)) # 0
print(num_steps(12)) # 3
print(num_steps(23)) # 2
print(num_steps(1024)) # 31
"""

INPUT_FILE_PATH = "input.txt"

def main():
    with open(INPUT_FILE_PATH) as f:
        n = int(f.readline())

    print(num_steps(n))

