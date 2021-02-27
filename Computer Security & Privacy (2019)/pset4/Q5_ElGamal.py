from pset_4_helper_functions import*
from random import randint

from hashlib import sha256





def key_gen(prime_bit_size):
    p = generate_n_bit_prime(prime_bit_size) # 300 bit prime
    q = 2*p + 1
    #print("p is", p)


    while rabin_miller(q, 40) == False:
        p = generate_n_bit_prime(prime_bit_size) # 300 bit prime
        q = 2*p + 1

    print("p is", p)
    print("q is", q)

    g = find_primitive_root_for_special_case(q) # a primitive_root mod q
    g = (g**2)%q

    a = randint(2,p-1)

    h = square_and_multiply(g, a, q)

    public_key = [q,g,h]
    private_key = [a]

    return(public_key, private_key)


def message_string_to_bits(message_file_name): # by convention we store message is in file 'message.txt'

    file = open(message_file_name, "r")

    message_ascii = ""
    for line in file:
        message_ascii = message_ascii + line
    file.close()

    message_as_bin = ""

    for char in message_ascii:
        m = bin(ord(char))[2:]
        while len(m) < 8:
            m = "0" + m
        message_as_bin = message_as_bin + m

    return(message_as_bin)


def sign(message_file_name, public_key, private_key, sign_with_hash_flag = False):

    if sign_with_hash_flag == True:
        file = open(message_file_name, "r")
        message_stream = ""

        for line in file:
            message_stream = message_stream + line

        file.close()

        #print("message stream is:", message_stream)


        hash_of_message_stream= sha256(message_stream.encode('ascii')).hexdigest()  # this line of code pointed out by  Paul Kurain, collaborator

        #print("hash is:", hash_of_message_stream)

        hash_as_int = ""

        for char in hash_of_message_stream:  #each ascii char converted to equivalent int.
            hash_as_int += str(ord(char))

        m = int(hash_as_int)


    else:
        message_as_bin = message_string_to_bits(message_file_name)
        m = int(message_as_bin,2)


    q, g, h = public_key[0], public_key[1], public_key[2]
    a = private_key[0]

    p = (q-1)//2
    k = randint(2, p-1)

    r = square_and_multiply(g, k, q)

    s = (m - a*r)%p
    s = ( s*find_modular_inverse(k, p) )%p

    signature = [r, s]
    return(signature)


def verify(message_file_name, public_key, signature, sign_with_hash_flag = False):
    if sign_with_hash_flag == True:
        file = open(message_file_name, "r")
        message_stream = ""

        for line in file:
            message_stream = message_stream + line

        file.close()


        hash_of_m = sha256(message_stream.encode('ascii')).hexdigest()  # this line of code pointed out by  Paul Kurain, collaborator

        hash_as_int = ""

        for char in hash_of_m:
            hash_as_int += str(ord(char))

        m = int(hash_as_int)


    else:
        message_as_bin = message_string_to_bits(message_file_name)
        m = int(message_as_bin,2)

    print("in verification, m is", m)
    q, g, h = public_key[0], public_key[1], public_key[2]
    r, s = signature[0], signature[1]

    if square_and_multiply(g, m, q) == (square_and_multiply(h,r,q)*square_and_multiply(r,s,q))%q:
        return(True)
    else:
        return(False)



def existential_forgery(message_file_name, public_key):

    q, g, h = public_key[0], public_key[1], public_key[2]
    p = (q-1)//2

    z = randint(2, p-1)

    r = (pow(g,z,q)*h)%q
    s = -r%p

    m = (z*s)%p


    '''modify message.txt to account for the forged random message'''

    #print("m as int:", m)

    m_as_chars = []

    m_as_bin = bin(m)[2:]

    while len(m_as_bin)%8 != 0:
        m_as_bin = "0" + m_as_bin

    #print("m_as_bin:", m_as_bin)

    m_as_chars = [ chr(int(m_as_bin[i:i+8], 2)) for i in range(0, len(m_as_bin),8)]

    #print("m_as_chars", m_as_chars)


    file = open(message_file_name, "w")
    for char in m_as_chars:
        file.write(char)  # the characters MAY NOT BE READABLE in file !

    file.close()


    fake_signature = [r,s]
    #check verification

    verification = verify(message_file_name, public_key, fake_signature, sign_with_hash_flag = False)

    print("verification of false signature yields:", verification )





if __name__== '__main__':
    key_gen_output = key_gen(prime_bit_size = 300) # set to 300
    #print(key_gen_output)

    public_key, private_key = key_gen_output[0], key_gen_output[1]
    # public key is a list of form   [q, g, h].  Private key is a list of form [a]




    message_file_name  = "message.txt"


    """ IMPORTANT:   When running a  case, make sure all other  cases are commented out"""




    # Test case 1: exitential forgery
    #''' 
    existential_forgery(message_file_name, public_key)
    # '''



    '''
    # Test case 2: Sign the hash
    signature = sign(message_file_name, public_key, private_key, sign_with_hash_flag = True)
    print("signature is:", signature)


    verification = verify(message_file_name, public_key, signature, sign_with_hash_flag = True)
    print(verification)
    '''
