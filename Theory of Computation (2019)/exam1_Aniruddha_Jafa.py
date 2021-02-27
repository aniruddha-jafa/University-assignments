''' TOC in-class programming exam 1        '''
import csv


# this code was written during a timed in-class exam
def simulate_NFA(input_string, delta_function, final_states):
    num_states = len(delta_function)
    states = sorted(list(delta_function.keys()))
    active_states = [0]  #q0 is active at the start
    active_states += delta_function[0]['e']   #all epsilon arrows leading from q0 are active at the start

    #print('At the start, active states are', active_states)

    for char in input_string:
        #print("input character", char)

        temp = [] # will be used to keep track of the next et of active states
        for state in active_states: # each state is an integer

            if state != 0:
                e_jumps = delta_function[state]['e']
                #print("e_jumps are", e_jumps)
                temp += delta_function[state]['e'] # make sure you account for the epsilon arrows


            temp += delta_function[state][char] # new states traversed at this stage based on the character we have
            #print(state, delta_function[state][char])

        active_states = list(set(temp)) # remove all repeated elements

        unexamined_e_jumps = active_states

        #print("Currently the active states are", active_states)

        while len(unexamined_e_jumps) > 0:  # while unexamined jumps is not empty
            current_jump_state = unexamined_e_jumps[0]
            #print("Current jump state being examined", current_jump_state)

            new_e_jumps = delta_function[current_jump_state]['e']

            unexamined_e_jumps = unexamined_e_jumps + new_e_jumps # get e jumps of this state

            active_states = active_states + new_e_jumps
            #print("Active state, new e_jump", active_states, new_e_jumps)

            unexamined_e_jumps.pop(0)

        active_states = list(set(active_states))

        #print("after accounting for e-jumps, active states are", active_states)


        print()

    print('Active states at the end of the run are', active_states)

    is_accepted = False
    for state in active_states:
        if state in final_states:
            is_accepted = True
            break

    return(is_accepted)



def detect_if_x1_substring_of_x2(x1,x2):
    if len(x1) == 0:
        return(True)


    else:
        delta_function = {}
        final_states = []

        # initliase delta_function

        for i in range(len(x2)+1):
            delta_function[i+1] = {'0':[], '1':[], 'e':[]}
            final_states.append(i+1)

        for i in range(len(x2)):
            char = x2[i]
            next_hop = []
            next_hop.append(i+2)
            delta_function[i+1][char] = next_hop

        # account for q0 in delta function

        delta_function[0] = {'0':[], '1':[], 'e':[]}
        delta_function[0]['e'] = final_states

        print("delta function", delta_function)
        print("final states", final_states)


        return(simulate_NFA(x1, delta_function, final_states))

x1 = input("Enter string for x1: ")
x2 =  input("Enter string for x2: ")

print()

print("x1 is a substring of x2:", detect_if_x1_substring_of_x2(x1,x2))
