def binary_string_to_int_array(binary_string):
    output = map(int, list(binary_string) ) # output is now a map type object
    return list(output)

def int_array_to_binary_string(int_array):
    output = ''.join(map(str,int_array))
    return output

def array_bytes_to_int_array(message):
    return list(map(int, ''.join(message)))

def int_array_to_array_bytes(CRC_remainder):
    CRC_remainder = int_array_to_binary_string(CRC_remainder)
    CRC_remainder_as_bytes = [] # an array fo bytes
    for i in range(0, len(CRC_remainder), 8):
        CRC_remainder_as_bytes.append(CRC_remainder[i:i+8])


def XOR(a,b): # assume a and b are either 0 or 1, integers
    output = (a-b)%2
    return output


# inspired from: https://en.wikipedia.org/wiki/Cyclic_redundancy_check#CRC-32_algorithm
def compute_CRC_remainder(message, CRC_poly):
    # INPUTS:
       # assume message is an array of bytes.
       # assume CRC_poly is a string.

    # OUTPUT: output is the remainder (as a an array of byes) of the division of the message by the CRC_poly

    message = array_bytes_to_int_array(message)
    CRC_poly = binary_string_to_int_array(CRC_poly)

    message_length = len(message)
    degree_CRC = len(CRC_poly) - 1 # Assume CRC_poly always has a leading 1. Hence degree_CRC = len(CRC) - 1

    #---- pad message with degree_CRC number of bits
    padded_message = message

    for i in range(degree_CRC):
        padded_message.append(0)

    while 1 in padded_message[0:message_length]:
        # exclude the padded bits i.e. it's fine if 1is in the padded bits
        # i.e. while there's a leading 1 large enough for us to divide,

        current_shift = padded_message.index(1)
        # gives first instance where index is 1

        for i in range(len(CRC_poly)):
            padded_message[current_shift + i] = XOR(padded_message[current_shift + i], CRC_poly[i])

    CRC_remainder = padded_message[message_length:] # returns the last degree_CRC bits of padded_message
    CRC_remainder = int_array_to_binary_string(CRC_remainder)

    CRC_remainder_as_bytes = [] # an array fo bytes

    for i in range(0, len(CRC_remainder), 8):
        CRC_remainder_as_bytes.append(CRC_remainder[i:i+8])

    return CRC_remainder_as_bytes


if __name__ == "__main__":

    test_1 = compute_CRC_remainder('11010011101100','1011')
    test_2 = compute_CRC_remainder('1101','1101')

    print(test_1)

    print(test_2)
