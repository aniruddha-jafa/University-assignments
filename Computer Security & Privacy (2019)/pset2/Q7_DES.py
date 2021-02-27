S_boxes = [[None, None, None, None] for i in range(8)]

S_boxes[0][0] = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7]
S_boxes[0][1] = [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8]
S_boxes[0][2] = [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0]
S_boxes[0][3] = [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]

S_boxes[1][0] = [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10]
S_boxes[1][1] = [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5]
S_boxes[1][2] = [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15]
S_boxes[1][3] = [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]

S_boxes[2][0] = [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8]
S_boxes[2][1] = [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1]
S_boxes[2][2] = [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7]
S_boxes[2][3] = [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]

S_boxes[3][0] = [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15]
S_boxes[3][1] = [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9]
S_boxes[3][2] = [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4]
S_boxes[3][3] = [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]

S_boxes[4][0] = [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9]
S_boxes[4][1] = [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6]
S_boxes[4][2] = [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14]
S_boxes[4][3] = [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]

S_boxes[5][0] = [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11]
S_boxes[5][1] = [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8]
S_boxes[5][2] = [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6]
S_boxes[5][3] = [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]

S_boxes[6][0] = [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1]
S_boxes[6][1] = [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6]
S_boxes[6][2] = [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2]
S_boxes[6][3] = [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]

S_boxes[7][0] = [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7]
S_boxes[7][1] = [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2]
S_boxes[7][2] = [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8]
S_boxes[7][3] = [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]


#================== Helper functions are below ============= #

def get_text_as_string_from_file(filename):
    file = open(filename, "r")
    text_as_string = ""
    for line in file:
        text_as_string = text_as_string + line.rstrip("\n")
    return(text_as_string)


def padded_plaintext_in_binary_to_ASCII_chars(binary_string):
    '''
    Input:
    the padded plaintext in binary, as a contiguous string

    Output:
    The plaintext as a contiguous string in ASCII. The padded bytes at the end (at most 8) have been converted to spaces.

    '''
    if len(binary_string)%8 != 0:
        print("Error, not divisible by 8")

    else:
        padded_plaintext_in_bytes = [binary_string[i:i+8] for i in range(0,len(binary_string),8) ]
        plaintext_ASCII = ""

        block_number = 0
        number_64_bit_blocks =  len(padded_plaintext_in_bytes)

        for byte in padded_plaintext_in_bytes: # set of bytes as all bytes of the padded plaintext
            byte_as_int = int(byte,2)

            if block_number <  (number_64_bit_blocks - 8) or byte_as_int > 8:
                plaintext_ASCII = plaintext_ASCII + chr(byte_as_int)

            else:                                     # take care of last few padding bytes (at most 8) in present in the last 64-bit block in plaintext, which are in decimal are ints from 1 to 8 in decimal
                plaintext_ASCII = plaintext_ASCII +  chr(32)      # chr(32) is a space; insert a space by default.

            block_number += 1

        return(plaintext_ASCII)


def char_to_byte_string(char):
    return(bin(ord(char))[2:].zfill(8))

def string_ASCII_chars_to_binary_string(string):
    # 1) each char converetd to byte string (len 8), then return all the strings joined together
    list_of_char_to_bytes = [char_to_byte_string(char) for char in string]
    ascii_chars_as_binary_string = ''.join(list_of_char_to_bytes)
    return(ascii_chars_as_binary_string)


def XOR_binary_strings(string1, string2):
    length = len(string1)
    return(bin(int(string1, 2) ^ int(string2, 2))[2:].zfill(length))        # return a string of len(string1)=len(string2) chars


# =================== Functions related to the DES Feistel Network ============= #

def plaintext_to_padded_binary(plaintext):
    '''
    Input:  assume plaintext is a contiguous string e.g. "romeoandjulietweregreatlovers"
    - convert each char in plaintext to 8-bit ascii binary rep
    - pad plaintext_as_binary using PKCS5
    - convert plaintext_as_binary to an array, a list of strings with each string being a 64-bit chunk

    Output:
    - a list of strings,each string being a 64-bit chunk
    '''

    # 1) convert each char to it's binary representation as a string, e.g. 'r' becomes '01110010'
    plaintext_as_binary = ""

    for char in plaintext:
        char_as_bin = char_to_byte_string(char) #convert to binary string, len 8
        plaintext_as_binary += char_as_bin

    # 2) Pad plaintext_as_binary with PKCS5 padding
    pad_value = (8 - len(plaintext)%8)

    print("PAD VALUE:", pad_value)
    pad_value_byte = bin(pad_value)[2:].zfill(8) # pad with 0s to the left till it's 8 bits long

    for i in range(pad_value):
        plaintext_as_binary += pad_value_byte

    # 3) Return plaintext_as_binary an array of strings with chunks of 64 bits each (8 bytes),
    # to make future processing easier (accesing blocks of 64 bits)

    plaintext_as_binary = [plaintext_as_binary[i:i+64] for i in range(0, len(plaintext_as_binary), 64)]  # List comprehension inspired from:  https://stackoverflow.com/questions/9475241/split-string-every-nth-character

    return(plaintext_as_binary)


def generate_key_schedule(key):
    '''
    Input:
    - a 7 character key as a string, which represents a 56 bit key

    Output:
    - key_schedule, a list of 16 keys. Each key is a binary string of len 48
    '''

    if len(key) != 7 :
        print("Error. Need key as a string of exactly 7 characters")

    else:

        # 1) convert to a 56 character string, which denotes the binary representation

        key = string_ASCII_chars_to_binary_string(key)

        key_schedule = [None for i in range(16)]                                            # initilaise, one key for each of the 16 rounds

        k =  [key[i:i+8] for i in range(0,56,8)]                                            # k has 7 bytes in total, k is the key schedule as a list of bytes
                                                                                            # k has been named 'k' because a shorter variable name was helpful for coding the left shift

        # 2) Get 16 roundkeys
        for i in range(16):

            #2.1) left shift k
            k[0],k[1],k[2],k[3],k[4],k[5],k[6] = k[2],k[3],k[4],k[5],k[6],k[0],k[1]

            round_key = [None for i in range(6)]                                         # will be an list of strings, each element is string that represents a byte, i.e. 48 bits in total.


            # 2.2) read first 3 bytes, last 3 bytes (first 24 bits, last 24 bits)
            round_key[0],round_key[1],round_key[2],round_key[3],round_key[4],round_key[5] = k[0],k[1],k[2],k[4],k[5],k[6]

            round_key_as_string = ''.join(round_key)                                     # convert to a string, len is 48
            key_schedule[i] = round_key_as_string

        return(key_schedule)                                                              # returns a list of 16 round_key, each round_key is a string of 48 chars


def expand_block(block):
    '''
    Input: a string of len 32, representing a block of 32 bits
    Output: a string expanded into 48 bit
    '''

    if len(block) != 32:
        return("Error, incorrect block size.")

    else:
        expanded_block = [None for i in range(48)]
        array_of_expansion_indexes= [
        31, 0, 1, 2, 3, 4,
        3, 4, 5, 6, 7, 8,
        7, 8, 9, 10, 11, 12,
        11, 12, 13, 14, 15, 16,
        15, 16, 17, 18, 19, 20,
        19, 20, 21, 22, 23, 24,
        23, 24, 25, 26, 27, 28,
        27, 28, 29, 30, 31, 0]

        for i in range(48):
            index = array_of_expansion_indexes[i]
            expanded_block[i] = block[index]

        expanded_block = ''.join(expanded_block)

        if len(expanded_block) != 48:
            print("Error in exapnded_block size")

        return(expanded_block)                                                       # return a 48 char string representing bits


def Sbox_substitution(block):
    '''
    Intput:
    - string of len 48, each char in the string represents a single bit

    Output:
    -  set_of_substitutions, a string of len 32
    -  obtained after applying S box substitution to 6-bit chunks of Input
    '''

    global S_boxes

    if len(block) != 48:
        print("Error, incorrect block size for Sbox_substitution")

    else:
        #  1) break 48 bit block into 8 groups of 6 bits each
        list_6_bit_sub_blocks = [block[i:i+6] for i in range(0,48,6)]
        set_of_substitutions = [None for i in range(8)]                                  # each element will be a 4-char string

        # 2) Perform the appropriate Sbox substitution on each of the 8 groups of 6 bits each
        for i in range(8):
            current_block = list_6_bit_sub_blocks[i]                                     # 6 bits as a string "b0,b1,b2,b3,b4,b5"
            s_box_to_access = i

            row_number = int(current_block[0] + current_block[5],2)                      # obtained from b0 and b5
            column_number = int(current_block[1:5],2)                                    # obtained from b1,b2,b3,b4

            s_box_substitution = S_boxes[s_box_to_access][row_number][column_number]     # s_box_substitution yields an int from 0-15.
            s_box_substitution = bin(s_box_substitution)[2:].zfill(4)                    # convert int in s_box_substitution to a binary string of 4 chars
            set_of_substitutions[i] = s_box_substitution

        set_of_substitutions = ''.join(set_of_substitutions)                             # convert to a contiguous string of len 32

        return(set_of_substitutions)                                                     # return a 32 char string representing bits


def Pbox_permutation(block):
    '''
    Input:
    a 32 bit string

    Output:
    a 32 bit string after permutation has been applied
    '''

    permutation_indexes = [
    15, 6, 19, 20, 28, 11, 27, 16,
    0, 14, 22, 25, 4, 17, 30, 9,
    1, 7, 23, 13, 31, 26, 2, 8,
    18, 12, 29, 5, 21, 10, 3, 24]

    permuted_Input = [None for i in range(32)]

    for i in range(32):
        permutation_index = permutation_indexes[i]
        permuted_Input[i] = block[permutation_index]

    permuted_Input = ''.join(permuted_Input)

    return(permuted_Input)                                                        # return a 32 char string representing bits


def feistel_function(block, round_key):
    '''
    Input:
    - block and round_key, 48 char strings

    Output:
    - 32 char string, the block after expand_block, XORing with round_key, Sbox_substitution, Pbox_permutation
    '''

    if len(block) != 32 or len(round_key) != 48:
        print("Error: feistel_function called with incorrect block or round_key length ")

    else:
        # 1) Expand 32 char string to string of 48 chars
        block = expand_block(block)

        # 2) Key mixing with 48 char key
        XORed_block = XOR_binary_strings(block, round_key)

        # 3) Use S_Box, get back a 32 bit string
        substituted_block = Sbox_substitution(XORed_block)

        # 4) Fixed permutation accorind to P_box
        permuted_block = Pbox_permutation(substituted_block)

        return(permuted_block)                                                  # returns a 32 char string representing bits


def feistel_network(block, key_schedule,  inialisation_vector = None, decryption_flag = False):
    '''
    Input: a 64 bit block (either padded plaintext or ciphertext, based when it's called); optional initialisation vector (for encryption), and a decryption flag
    Output: The blcok processed through 16 rounds of the feistel function.
    '''

    if decryption_flag == False:
        block_XORed_with_IV =  XOR_binary_strings(block, inialisation_vector)
        left_block, right_block = block_XORed_with_IV[0:32], block_XORed_with_IV[32:]                # 32 bit strings


    elif decryption_flag == True:                                                                    # Meant for decryption in ECB. Don't use inialisation_vector inside feistel_network while decrypting
        left_block, right_block  = block[0:32], block[32:]
        key_schedule = key_schedule[::-1]                                                            # use reverse key schedule for decryption

    for i in range(16):
        round_key = key_schedule[i]


        temp = right_block
        right_block =   XOR_binary_strings(left_block, feistel_function(right_block, round_key))  # R_(i+1) = L_i XOR f(R_i, K_i)
        left_block = temp                                                                         # L_(i+1) = R_(i)

                                                                                                  # swap R and L, to make decryption possible through the same feistel function

    return(right_block + left_block)                                                              # return a 64 char string


# =============== Functions for encryption and decryption ============= #

def des_encryption(plaintext, key, inialisation_vector):
    '''
    Input:
    - plaintext, key, inialisation_vector. All 3 are strings.

    Output:
    - set_of_ciphertexts, a list where each element is a 64 char ciphertext
    '''

    if len(inialisation_vector) != 8 or len(key) != 7:
        print("Error: incorrect size of inialisation_vector, or key")

    else:
        print("Encrypting the following plaintext:", plaintext)
        print("Len plaintext is:", len(plaintext))
        # 1) Convert plaintext to binary, PKCS5 padding
        padded_plaintext_in_64_bit_blocks = plaintext_to_padded_binary(plaintext)
        print("padded_plaintext_in_64_bit_blocks is:", padded_plaintext_in_64_bit_blocks)
        print()

        # 2) Generate key_schedule
        key_schedule = generate_key_schedule(key)
        print("key_schedule is", key_schedule)
        print()

        # 3) Initialise current_IV, 64 char string representing bits
        current_IV = string_ASCII_chars_to_binary_string(inialisation_vector)
        print("First IV is:", current_IV)

        # 4) Run each block through Fiestel network
        set_of_ciphertexts = []                                                             # list of 64-char strings, each string being a ciphertext corresponding to a block in the padded Input

        for block in padded_plaintext_in_64_bit_blocks:                                     # each block is a 64-char string

            # 4.1) Obtain ciphertext after running through feistel_network
            ciphertext_of_current_block = feistel_network(block, key_schedule, current_IV)  # 64 bit string

            set_of_ciphertexts.append(ciphertext_of_current_block)

            # 4.2) update IV
            current_IV = ciphertext_of_current_block                                         # current_IV is a 64-char string




        # 5) Write each ciphertext to cipher.txt, each line gets a 64-bit ciphertext.
        ciphertext_file = open("ciphertext.txt","w")

        for ciphertext in set_of_ciphertexts:
            ciphertext_file.write(ciphertext + "\n")
        ciphertext_file.close()

        # 6) return set_of_ciphertexts
        return(set_of_ciphertexts)                                                            # returns a list of ciphertexts,


def des_decryption(ciphertext_stream, key, inialisation_vector):
    '''
    Input: A stream of ciphertext, a large string obtained from ciphertext.txt using function get_text_as_string_from_file

    Output: the plaintext corresponding to the ciphertetx, as a string. Also writes plainetxt to plaintext.txt
    '''

    if len(ciphertext_stream)%64 != 0:
        print("Error, ciphertext_stream is not divisible by 64. Need 64-bit blocks")
        return(False)

    set_of_ciphertexts = [ciphertext_stream[i:i+64] for i in range(0,len(ciphertext_stream), 64)]  # blocks of 64

    # 1) Generate key schedule
    key_schedule = generate_key_schedule(key)
    set_of_decryptions = []

    # 2) XOR with IV's after calling feistel_network.
    # Order of IVs is:  initialisation_vector, ciphertext_1, ciphertext_2 .... ciphertext_(n-1)
    current_IV = string_ASCII_chars_to_binary_string(inialisation_vector)

    # 3) Run through feistal network
    for i in range(len(set_of_ciphertexts)):
        cipher_block = set_of_ciphertexts[i]

        decryption = feistel_network(cipher_block, key_schedule, decryption_flag = True)
        decryption_XORed_with_current_IV = XOR_binary_strings(decryption, current_IV)     # In ECB decryption, first run through feistel_network, then XOR with an IV

        set_of_decryptions.append(decryption_XORed_with_current_IV)
        current_IV = cipher_block

    print("After decryption, 64 bit blocks of padded plaintext:")
    for i in set_of_decryptions:
        print(i)

    set_of_decryptions = ''.join(set_of_decryptions)                                      # convert to string


    # 4) Get the plaintext
    plaintext = padded_plaintext_in_binary_to_ASCII_chars(set_of_decryptions)

    # 5) Write to plaintext.txt
    plaintext_file = open("plaintext.txt", "w")
    plaintext_file.write(plaintext)

    return(plaintext)                                                                     # returns the decrypted plaintext as a string, after writing it to plaintext.txt



if __name__ == "__main__":

    key = get_text_as_string_from_file("key.txt")
    initialisation_vector = "abcdefgh"

    # ------- Perform DES encryption here after uncommenting the following 3 lines. Comment out all decryption lines ----- #
    #plaintext =  get_text_as_string_from_file("plaintext.txt")
    #set_of_ciphertexts = des_encryption(plaintext, key, initialisation_vector)
    #print("\nSee ciphertext.txt for ciphertext")


    # ------- Perform DES decryption here, after uncommenting the following 3 lines. Comment out all encyption lines ----- #
    ciphertext_stream = get_text_as_string_from_file("ciphertext.txt")
    des_decryption(ciphertext_stream, key, initialisation_vector)
    print("\nSee plaintxt.txt for decryption in ASCII chararacters")
