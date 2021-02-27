import numpy as np



# binary sigmoid, maps inputs from 0 to 1
def binary_sigmoid(S,b): # keep optional argument for parameter

    value = ( 1 / ( 1 +  (np.e)**(-S) ) )
    return value


def derivative_of_binary_sigmoid(S, b): # keep optional argument for parameter; may use it later

    binary_sigmoid_value = ( 1 / ( 1 +  (np.e)**(-S) ) )

    derivative = binary_sigmoid_value*( 1 - binary_sigmoid_value)

    return derivative
