
from random import randint, getrandbits

# slide 5-1, p. 20/32.
def square_and_multiply(a,b,n):
# output a^b  mod(n).
# Meant to be an equivalent to inbuilt pow(a,b,c), which does a^b mod c

    r = 1

    while b > 0:
        if b%2 == 1: # least to most significant bit
            r = (r*a) % n
        b = b//2
        a = (a*a)%n

    return(r)


def find_modular_inverse(a,n): # find a^(-1) mod n, if it exists
    output_from_extended_euclidean = extended_euclidean(a,n)

    gcd = output_from_extended_euclidean[0]

    if gcd != 1:
        print("inverse of a doesn't exist mod n, a and n are: ", a, n)
        return(False)

    else:
        return(output_from_extended_euclidean[1]%n)


# pseudocode from:  https://brilliant.org/wiki/extended-euclidean-algorithm/
# Used for finding modular inverse
def extended_euclidean(a,b):

    r1 = abs(a)
    r2 = abs(b)

    # initialise [u1 u2] and [v1 v2]
    v1 = 0
    if a < 0:
        u1 = -1
    else:
        u1 = 1

    u2 = 0
    if b < 0:
        v2 = -1
    else:
        v2 = 1

    #print("initilisation u1 v1", u1,v1)
    #print("initilisation u2 v2", u2,v2)

    while r2 != 0:
        q = r1//r2

        r1, r2 = r2, r1 - q*r2
        u1, u2 = u2, u1 - q*u2
        v1, v2 = v2, v1 - q*v2

    # print("r1 is", r1)   # r1 is the gcd, actually

    return([r1, u1, v1])  # Get Bezout coefficients  u, v such that au + bv = gcd(a,b)

def check_if_quadratic_residue(a, p): # Euler criterion, non-trivial QR  iff   a^(p-1)/2 = 1 mod p
                                      # p is an odd prime
    if square_and_multiply(a,(p-1)/2, p) != -1%p:
        return(True)
    else:
        return(False)


def find_square_roots_of_quadratic_residue(a, p):  # mix of Shanks algorithm, and a shortcut when p = 3 (mod 4)
    '''
    inputs:
    a is a QR (we'll check this),
    p is an odd prime

    '''

    if check_if_quadratic_residue(a,p) == False:
        print("input is not a QR mod p, so no roots can be found")
        return(False)

    if a%p == 0:
        print("A is a trivial QR")
        return([0])

    # A shortcut,  from Lecture 13 extra, 18/54
    if (p + 1)%4 == 3:
        b = square_and_multiply(a, (p+1)//4, p)   # square roots mod p are b and -b
        return([b, -b%p])


    else: # Shanks algorithm

        # Method to find s and t. Taken from slides lec 8-2, 49.
        s = 0
        t = p-1

        while t%2 == 0:    # maintains invariant,  2^s.t = p-1
            s += 1
            t = t//2

        # generate random u such that u in QNR_p
        u = randint(1, p-1)  # random integer from 1 to p - 1
        while check_if_quadratic_residue(u,p) == True:
            u = randint(1, p-1)

        k = s
        z = square_and_multiply(u, t, p)
        x = square_and_multiply(a, (t+1)//2, p)
        b = square_and_multiply(a, t, p)


        while b%p != 1:

            # find m such that m is least integer such that b^(2^m) =  1 (mod p)
            temp = b
            m = 0
            while (temp)%p != 1:
                temp = (temp*temp)%p
                m += 1

            y = square_and_multiply(z, pow(2,k-m-1), p)
            z = (y*y)%p
            b = (b*z)%p
            x = (x*y)%p
            k = m

        return([x, -x%p])


# pseudocode from https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test, and
# https://brilliant.org/wiki/prime-testing/#miller-rabin-primality-test
def rabin_miller(bit_size, repeat_times = 5):
    n = bit_size

    if n%2 == 0 or n <= 1:
        return False

    #----  express n-1 as   2^s.t, s is a +ve int, t is an odd int.

    # Method to find s, t taken from slides lec 8-2, 49.
    s = 0
    t = n-1

    while t%2 == 0:    # maintains invariant,  2^s.t = n-1
        s += 1
        t = t//2

    #print("s,t: ", [s,t])
    for i in range(repeat_times):

        a = randint(2,n-1) # random integer in [2, n-2]
        x = square_and_multiply(a,t,n)  # x = a^t (mod n)

        if x == 1:
            continue   # if this condition is met skip, this iteration of the outer for-loop, pick a new a

        is_definitely_composite = True

        for k in range(s):  # check if any of a^t, a^(2t)......  a^(2^s.t)  = -1 mod n

            if  x == n-1:     # (x + 1) % n == 0 :    # check if  x = -1  mod n
                is_definitely_composite = False
                break
            else:
                x = square_and_multiply(x,2,n)  #   x = x^2 mod n = a^( 2^k . d) mod n

        if is_definitely_composite:
            #print("n is definitely composite, witness is", a)
            return(False)

    #print("n is probably prime, a is:",  a)
    return(True)

# referred to: https://medium.com/@prudywsh/how-to-generate-big-prime-numbers-miller-rabin-49e6e6af32fb, code was written on my own
def generate_n_bit_prime(bit_size):
    is_prime = False

    while is_prime == False:
        p = getrandbits(bit_size)
        mask_bit_string = 1 << (bit_size - 1) | 1  # number of the form 1000..0001, of len = bit_size
        p = p | mask_bit_string  # to make sure most significant bit is 1 (so it's actually an n-bit prime), least significant bit is 1 (so its odd)

        is_prime = rabin_miller(p, 40)

        #if is_prime == False:
            #print("discarded candidate:", p)

    #print("generated prime (with high probability) is:", p)
    return(p)



def find_primitive_root_for_special_case(q): # find a primitive root mod q, where q = 2p + 1,
    #print("q is", q)

    list_of_factors_of_q_minus_1 = [2, (q-1)//2]  # p = (q-1)/2 since q = 2p + 1
    #print("factors of q", list_of_factors_of_q_minus_1)

    found_primitive_root = False

    while found_primitive_root == False:

        g = randint(2, q-1)
        #print("cadidate g is:", g)

        is_primitive_root = True

        for h in list_of_factors_of_q_minus_1:
            #print (pow(g, power,p),g,power,p)
            power = int((q-1)/h)

            if  square_and_multiply(g,power,q) == 1:
                is_primitive_root = False
                break

        if is_primitive_root == True:
            found_primitive_root = True

    return(g)



if __name__ == '__main__':
    
    ''' Some test cases below:'''

    #print(find_modular_inverse(5,10))

    #print(find_square_roots_of_quadratic_residue(9,11))
    #print(find_square_roots_of_quadratic_residue(9,23))

    #print(find_primitive_root_for_special_case(11))
