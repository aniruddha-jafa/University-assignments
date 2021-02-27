import random
from Activation_function import *
import numpy as np
import matplotlib.pyplot as plt


# --------------  find  number_training_examples
number_training_examples = 0   # N: the number of training examples

with open("hw3trainingdata.txt",'r') as training_data:
    i = 0
    for line in training_data:
        number_training_examples += 1
print('Number of input lines', number_training_examples)


# --------------  initialise the numer of neurons or components at each layer
input_components = 1 # number of components of input
hidden_neurons = 4 # number of hidden layer neurons
output_neurons=  1 # number of neurons in output layer


# ---------------- initialise weight vectors
w_input_hidden = [ [0]*( input_components + 1) ] * hidden_neurons   # n_ rows of size n + 1 each; +1 is for the bias for each neuron at hidden layer.
W_hidden_output = [ [0]*( hidden_neurons )  ] * output_neurons # m rows of size n_ each. Not n_ + 1 beacuse there are no biases at output layer.


# ----------------  Populate weights with random values
a = -0.5
b = 0.5
for i in range(output_neurons):
    for j in range(hidden_neurons):
        W_hidden_output[i][j] = random.uniform(a,b)

for j in range(hidden_neurons):
    for k in range(input_components + 1): # n+1 becasue of the biases
        w_input_hidden[j][k] = random.uniform(a,b)


# ------------------ initialise some global variables



error_margin = 0.5 # set to 0.0.4
Cost = error_margin + 1 # initialise to some value so that the while loop can run
step_size = 0.03 # intialise eta
Epoch = 1
training_cost_array = []


#----------------------------------- Main loop for backpropagation algorthim --------------------------------#


while Cost > error_margin:

    training_data = open('hw3trainingdata.txt','r')

    Cost = 0 # set cost to zero for current Epochs

    for training_example in range(number_training_examples): # for each of the N inputs

        #------------- for current training example, get input and output

        input_vector = []
        desired_outputs = []

        for i in range(input_components): # n is number of input components, which here is the same as the number of output components
            input, output = training_data.readline().split()
            input, output = float(input), float(output)
            input_vector.append(input)
            desired_outputs.append(output)
        input_vector.insert(0,1) # put a 1 in the 0th index, which is the input for the bias

    #--------------------------------FORWARD PASS----------------------------#
        #-------------- Calculate Sum_input_hidden, and H_j.

        H_j = [0] * hidden_neurons
        Sum_input_hidden = [0] * hidden_neurons

        for j in range(0, hidden_neurons): # hidden neurons are 1,2..n_
            for k in range(0, input_components + 1): # n + 1 becasue of the bias weights. For each hidden neuron, there are 1,2...(n + 1) weights leading to it
                #print("index pair is:", j,k)
                #print("weight, input for Sum_input_hidden are", w_input_hidden[j][k], input_vector[k])
                Sum_input_hidden[j] += w_input_hidden[j][k]*input_vector[k]

            #print("Current Sum_input_hidden: {0}, j {1}:".format(Sum_input_hidden, j))
            H_j[j] = binary_sigmoid(Sum_input_hidden[j],1)

        #print("H_j's are given by:", H_j)

        #--------------- Calculate S_i and y_hat

        Sum_hidden_output = [0]* output_neurons # S_i
        estimated_outputs = [0]* output_neurons # y_hat

        for i in range(0, output_neurons): # for each of the m output neurons
            for j in range(0,hidden_neurons): # for each of the hidden layer neurons
                Sum_hidden_output[i] += W_hidden_output[i][j] * H_j[j]

            estimated_outputs[i] = binary_sigmoid(Sum_hidden_output[i],1)

        #print("estimated_outputs are given by", estimated_outputs)

        #----------------- Update Cost

        for i in range(0, output_neurons):
            Cost += (estimated_outputs[i] - desired_outputs[i])**2

        #print("Cost for example number {0} is: {1}".format(training_example+1, Cost))
        #print()

        #---------------------------------------BACKWARD PASS---------------------------------------#


        #------------- Calculate del_i, and del_j

        del_i = [0]* output_neurons  # each output layer neuron has a del_i
        del_j = [0]* hidden_neurons # each hidden layer neuron has a del_j

        for i in range(0,output_neurons):
            del_i[i] = ( desired_outputs[i]- estimated_outputs[i])*derivative_of_binary_sigmoid(Sum_hidden_output[i],1)

        for j in range(0,hidden_neurons):
            for i in range(0,output_neurons):
                del_j[j] += del_i[i] * W_hidden_output[i][j]*derivative_of_binary_sigmoid(Sum_input_hidden[j],1)

        # print("del_i: {0}, del_j: {1} ".format(del_i, del_j))

        # -------------------------------------- UPDATE WEIGHTS -------------------------------------- #

        for i in range(output_neurons):
            for j in range(hidden_neurons):
                W_hidden_output[i][j] = W_hidden_output[i][j] + ( step_size * del_i[i] * H_j[j] )

        for j in range(hidden_neurons):
            for k in range(input_components + 1): # n+1 becasue of the biases

                w_input_hidden[j][k] = w_input_hidden[j][k] + ( step_size * del_j[j] * input_vector[k] )

        #print("New W_ij = {0}\nNew w_ij = {1}".format(W_hidden_output, w_input_hidden))

    training_cost_array.append(Cost)
    print("=======> The Epoch is {0}, and the Cost is {1}".format(Epoch, Cost))
    Epoch += 1
    print()


    training_data.close()

""" Try to actually print the prediction for an input. Write a prediction function"""


# Plot error by epoch, use training_cost_array

print("training_cost_array:", training_cost_array)
plt.plot(training_cost_array)
plt.show()


# Estimate testing error on "hw3.txt"
