#
# rule90.py - an implementation of Cellular Automata - Rule 90
#
# Reddit: Daily Programmer - Easy - Challenge #213
#



# helper functions


def xor(left, right):

    int_left  = int(left)
    int_right = int(right)

    total = int_left + int_right

    if total == 2:

        return "0"

    elif total == 1:

        return "1"

    else:

        return "0"



def update_cell(state, i):

    left  = ""
    right = ""

    # determine left operand of xor

    if i - 1 < 0:

        left = "0"

    else:

        left = state[i-1]

    # determine right operand of xor

    if i + 1 >= len(state):

        right = "0"

    else:

        right = state[i+1]

    # compute actual xor value

    return xor(left, right)



def simulate_step(state):

    res = ""

    for i in range(0, len(state)):

        res += update_cell(state, i)

    return res



def state_to_stars(state):

    res = ""

    for i in range(0, len(state)):

        if state[i] == "0":

            res += " "
            
        else:

            res += "*"

    return res



# main logic

def main():

    next_state = raw_input("Enter an initial state (eg. 10010): ")

    num_iterations = int(raw_input("Number of steps to simulate: "))

    print

    print state_to_stars(next_state)

    for i in range(0, num_iterations):

        next_state = simulate_step(next_state)

        next_state_out = state_to_stars(next_state)

        print next_state_out

    print
