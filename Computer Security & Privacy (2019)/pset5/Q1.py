def pad_message(message_as_bits, r = 64):
  '''
  Input  message_as_bits: a string of bits, representing the mesage
         r:  size of each block. By default, r = 64
  Output padded output P, such that r | len(P)

  '''
  padded_message = message_as_bits + "1"      # append first 1
  zeroes_needed = (r - len(padded_message)%r) - 1
  padded_message = padded_message + zeroes_needed*"0" + "1"  # append 0s and last 1
  return(padded_message)

def xor_string(a,b):
  """
  Takes two strings and xors the individual bits of them together
  """
  if len(a) != len(b):
    print("Trying to XOR strings of unequal input")
    return(False)

  fill_len = len(a)

  return(bin(int(a, 2) ^ int(b, 2))[2:].zfill(fill_len))


def block_permutation_function(state):
    xor_with_this_string= "01001100100010100100010111100100110010110001111111110011101011100000110000010010001110110000111001111010010011101101001010000010"

    for i in range(20):
        state = xor_string(state, xor_with_this_string)

        shift_index = int(xor_string(state[:8], "0" + bin(101)[2:] ), 2)%128

        temp = state

        state = temp[shift_index:] + temp[:shift_index]


    return(state)



def SHA_3_for_noobs(message_as_bits, r = 64, b = 128, desired_output_length = 56):

  padded_message = pad_message(message_as_bits, r)
  print("padded_message, len(padded_message): ", padded_message, len(padded_message))

  padded_message_as_blocks = [padded_message[i:i+r] for i in range(0, len(padded_message), r)]
  print('padded_message_as_blocks: ', padded_message_as_blocks)

  state = b*"0"   # initialise starting state

  c = b - r

  # Absorption

  for block in padded_message_as_blocks:
      current_block = block + c*"0"    # pad till len current_block = r + c = b

      if len(current_block) != b:
          print("error, incorrect len")
          return(False)

      current_block = xor_string(current_block, state)
      state = block_permutation_function(current_block)


  output = ""   # initialise to empty string

  while len(output) < desired_output_length :
      output =  output +  state[0:r]

      if len(output) < desired_output_length:
          state = block_permutation_function(state)

  output = output[:desired_output_length]  # truncate to desired_output_length

  return(output)



if __name__ == "__main__":

    test_message = "011011010110111001100010"

    padded = pad_message(test_message, r = 64)
    #print("initial padded message is:", padded, " \n")

    padded = padded  + "0"*(128 - len(padded))
    #print("padded message is: ", padded)
    #print("len padded:", len(padded))

    permutation = block_permutation_function(padded)

    print('block permutation:', permutation)
    comparison_string = "00000000110011010001111101110010101011101110010011111110111111110110110110111101111011101100000100000100110011101011100101010011"

    print(permutation == comparison_string)

    print("-------------\n")


    print("SHA hash", SHA_3_for_noobs("1111", r = 64, b = 128, desired_output_length = 56))
