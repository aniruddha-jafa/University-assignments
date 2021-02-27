class e_NFA:
    # Each NFA is defined by the delta function and final states
    # the method simulate_NFA evalatues if an input string is accept by an NFA

    def __init__(self, delta_function, final_states):
        self.delta_function = delta_function # a dictionary of dictionaries
        self.final_states = final_states # a list

    def simulate_NFA(self, input_string):
        total_states = list(self.delta_function.keys())


        # 1) Initialse states that are active at the start of the machine
        active_states = [0]
        active_states += self.delta_function[0]['e']   #all epsilon arrows leading from q0 point to states that are active at the start

        print('At the start, active states are', active_states)

        #1.1) Account for chains of e jumps that may be active at the start
        unexamined_e_jumps = active_states # unexamined jumps will act as a Queue

        while len(unexamined_e_jumps) > 0: #and len(active_states) < len(total_states):
            current_state = unexamined_e_jumps[0]
            new_e_jumps = self.delta_function[current_state]['e']

            unexamined_e_jumps = unexamined_e_jumps + new_e_jumps # get e jumps of this state
            active_states = active_states + new_e_jumps
            active_states = list(set(active_states)) # remove repeated elements

            unexamined_e_jumps.pop(0) # dequeue the state you have examined

        print("After accounting for chains of e-jumps, active states at start are:", active_states)


        # 2) For each character in the input
        for char in input_string:
            temp = [] # will be used to keep track of the next et of active states

            # 2.1)  Account for jumps based on char
            for state in active_states:
                jumps_based_on_char = self.delta_function[state][char]
                temp = temp + jumps_based_on_char # new states traversed at this stage based on the character we have

            active_states = list(set(temp)) # remove all repeated elements
            print("char: {0}. Currently the active states are {1}".format(char, active_states))

            #------- 2.2) Account for sequences of e-jumps, given the states that are currently active
            unexamined_e_jumps = active_states # unexamined jumps will act as a Queue

            while len(unexamined_e_jumps) > 0: #and len(active_states) < len(total_states):
                current_state = unexamined_e_jumps[0]
                new_e_jumps = self.delta_function[current_state]['e']

                unexamined_e_jumps = unexamined_e_jumps + new_e_jumps # get e jumps of this state
                active_states = active_states + new_e_jumps
                active_states = list(set(active_states)) # remove repeated elements

                unexamined_e_jumps.pop(0) # dequeue the state you have examined

            print("After accounting for e-jumps, active states are: {1} \n".format(char, active_states))

        print('Active states at the end of the run are', active_states)

        # 3) Check if there are any final states active at the end of the run
        is_accepted = False
        for state in active_states:
            if state in self.final_states:
                is_accepted = True
                break

        return(is_accepted)

def update_delta_function(old_delta_function, offset):
    # Purpose: modify the mapping of delta function based on the offset (modified indices of the states)
    new_delta_function = {}
    charset = ["0","1","e"]

    for state in old_delta_function:
        new_delta_function[state + offset] = {}

        for char in charset:
            mapping = old_delta_function[state][char]  # an array, get values of mapping powerset

            for j in range(len(mapping)): #incriment each entry in array by 1
                mapping[j] = mapping[j] + offset

            new_delta_function[state + offset][char] = mapping

    return(new_delta_function)

def is_within_redundant_outermost_parentheses(input_string):
    # check if input string is within redundant outermost parentheses
    if input_string[0] == "(" and input_string[-1] == ")":
        count = 0
        is_within_redundant_parentheses = True

        for i in range(len(input_string)):
            char = input_string[i]
            if char == "(":
                count += 1
            elif char == ")":
                count -= 1
            else:
                pass

            # LOGIC: if left at right parentheses are 'balaned' before the last character is examined, there are no redundant parentheses
            if count == 0 and i < len(input_string) - 1:
                is_within_redundant_parentheses = False
                break
        return(is_within_redundant_parentheses)

    else:
        return(False)

def union_NFAs(NFA_1, NFA_2):
    delta_1 = NFA_1.delta_function
    delta_2 = NFA_2.delta_function
    final_states_1 = NFA_1.final_states
    final_states_2 = NFA_2.final_states

    delta_function_union = {}
    final_states_of_union = []
    offset_delta_2 = len(delta_1) + 1   # also gives index of start state of delta_2 in new machine

    # 1) take care of elements in delta_1
    delta_function_union = update_delta_function(delta_1, 1)

    # 2) take care of elemetns in delta_2
    temp = update_delta_function(delta_2, offset_delta_2)
    for state in temp:
        delta_function_union[state] = temp[state]


    # 3) update final_states_of_union
    for state in delta_1:
        if state in final_states_1:
            final_states_of_union.append(state + 1)

    for state in delta_2:
        if state in final_states_2:
            final_states_of_union.append(state + offset_delta_2)

    # 4) Lastly, define q0 for delta_function_union
    delta_function_union[0] = {'0':[], '1':[], 'e':[1, offset_delta_2] }

    print("delta_function_union is:",   delta_function_union)
    print("final_states_of_union are:", final_states_of_union)
    print()

    union_NFA = e_NFA(delta_function_union, final_states_of_union)

    return(union_NFA)

def concatentation_NFAs(NFA_1, NFA_2):
    delta_1 = NFA_1.delta_function
    delta_2 = NFA_2.delta_function
    final_states_1 = NFA_1.final_states
    final_states_2 = NFA_2.final_states

    delta_function_concat = {}
    final_states_of_concat = []
    offset_delta_2 = len(delta_1) # also gives index of delta_2's starting state, as represented in delta_function_concat

    # 1) take care of elements from delta_2
    delta_function_concat = update_delta_function(delta_2, offset_delta_2)

    # 2.1) take care of elements from delta_1
    for state in delta_1:
        delta_function_concat[state] = delta_1[state] # no offset required

        # 2.2) attach all final states in delta_1 to start state representing delta_2, whose index is given by offset_delta_2
        if state in final_states_1:
            start_state_index_delta_2 =  offset_delta_2
            delta_function_concat[state]['e'].append(start_state_index_delta_2)

    #3) Update final_states_of_concat based on final_states_2
    for state in delta_2:
        if state in final_states_2:
            final_states_of_concat.append(state + offset_delta_2)

    print("delta_function_concat is: ", delta_function_concat)
    concat_NFA = e_NFA(delta_function_concat, final_states_of_concat)

    return(concat_NFA)

def star_NFA(NFA_1):

    delta_func = NFA_1.delta_function
    final_states = NFA_1.final_states

    # 1)  build delta_function_star
    delta_function_star = {}
    delta_function_star = update_delta_function(delta_func, 1) # increase state indices with offset 1

    # 2) define q0 for delta_function_star
    delta_function_star[0] = {'0':[],'1':[],'e':[1]} # connect 'e' to conceptually connect to start state of NFA_1
    final_states_of_star = [0]  # q0 is a final sate to accept e

    # 3) update final states, and connect final states to start state of old machine
    for state in delta_func:
        if state in final_states:
            final_states_of_star.append(state + 1)
            delta_function_star[state + 1]['e'].append(1)  # 1 represents start state of old machine. Connect e arrows of final state to this.

    print("delta_function_star", delta_function_star)

    star_NFA = e_NFA(delta_function_star, final_states_of_star)
    return(star_NFA)

def find_index_of_main_operator(input_string):  # idea given by Vidur Singh
     # Goal:  find index of the U or . operator in the regex
    if len(input_string) == 3:   # expressions of form "1U0" or "0.1" etc
        return(1)

    else:
        depth_array = ['x']*len(input_string)
        count = 0

        # for each element in input_string that is not "(" or ")", define a depth based on count
        for i in range(len(input_string)):
            char = input_string[i]
            if char == "(":
                count += 1
            elif char == ")":
                count -= 1
            else:
                depth_array[i] = count

        #print("Level array:", depth_array)
        index_of_min_element = float("inf")
        min_element = float("inf")   # initialise as infinity

        for i in range(len(depth_array)):
            if i == 0 or i == len(depth_array) - 1: # operator can't be in first or last index (if there are parens), so pass
                pass
            elif depth_array[i] == 'x':   # a parenthesis occured, so marked as x in depth_array
                pass

            else:
                if depth_array[i] < min_element:
                    min_element = depth_array[i]
                    index_of_min_element = i

        index_of_main_operator = index_of_min_element
        return(index_of_main_operator)

def regex_to_NFA(input_string):
    # base case
    if len(input_string) == 1:
        print("Base case with string: ",input_string)
        if input_string == '1':
            delta_function = {
            0:{'0':[],'1':[1],'e':[]},
            1:{'0':[],'1':[],'e':[]}
            }
            final_states = [1]
            NFA_that_accepts_1 = e_NFA(delta_function, final_states)
            return(NFA_that_accepts_1)

        elif input_string == '0':
            delta_function = {
            0:{'0':[1],'1':[],'e':[]},
            1:{'0':[],'1':[],'e':[]}
            }
            final_states = [1]
            NFA_that_accepts_0 = e_NFA(delta_function, final_states)
            return(NFA_that_accepts_0)

        else:
            print("ERROR - function called on invalid input", input_string)

    else:
        # last character is a star
        print()
        print("Evaluating string:", input_string)

        if is_within_redundant_outermost_parentheses(input_string) == True:
            print("REDUNDANT parentheses deteced")
            input_string_without_outermost_parentheses = input_string[1:-1]
            return(regex_to_NFA(input_string_without_outermost_parentheses))

        elif input_string[-1] == "*":
            print("STAR detected in string", input_string)
            input_to_be_starred = input_string[:-1]
            return(star_NFA(regex_to_NFA(input_to_be_starred)))

        else:
            index_of_main_operator = find_index_of_main_operator(input_string)
            main_operator = input_string[index_of_main_operator]
            print("index_of_main_operator is {0}, main operator is {1}".format(index_of_main_operator, main_operator))

            if main_operator == "U":
                left_child = input_string[0:index_of_main_operator]
                right_child = input_string[index_of_main_operator+1:]
                print("left_child, right_child:", left_child, right_child)

                NFA_of_union = union_NFAs(regex_to_NFA(left_child), regex_to_NFA(right_child))
                return(NFA_of_union)

            elif main_operator == ".":
                left_child = input_string[0:index_of_main_operator]
                right_child = input_string[index_of_main_operator+1:]
                print("left_child, right_child:", left_child, right_child)

                NFA_of_concat = concatentation_NFAs(regex_to_NFA(left_child), regex_to_NFA(right_child))
                return(NFA_of_concat)

            else:
                print("ERROR - invalid main operator")

if __name__=="__main__":

    regex = "1U((0.(1.0))*)"  #"(1.((0.0)*))U0"  # ENTER input regex here

    my_NFA = regex_to_NFA(regex)

    print("\n --------------- \n")

    string_to_check =  "010010" # ENTER string to check

    answer = my_NFA.simulate_NFA(string_to_check)

    print(" --------------- ")

    print("Answer is: ", answer )
