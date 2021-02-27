'''

TO DO:

- test cases for Rabin Miller
'''

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


# pseudocode from:  https://brilliant.org/wiki/extended-euclidean-algorithm/

def extended_euclidean(a,b):

    r1 = abs(a)
    r2 = abs(b)

    # initilise [u1 u2] and [v1 v2]
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

    return([u1,v1])  # Get Bezout coefficients  s,t such that as + bt = gcd(a,b)



# pseudocode from https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test, and
# https://brilliant.org/wiki/prime-testing/#miller-rabin-primality-test
def rabin_miller(n, repeat_times = 1):

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
            print("n is definitely composite, witness is", a)
            return False

    #print("n is probably prime, a is:",  a)
    return True


# referred to: https://medium.com/@prudywsh/how-to-generate-big-prime-numbers-miller-rabin-49e6e6af32fb, code was written on my own
def generate_n_bit_prime(bit_size):
    is_prime = False

    while is_prime == False:
        p = generate_n_bit_number(bit_size)
        is_prime = rabin_miller(p, 64)

        if is_prime == False:
            print("discarded candidate:", p)

    print("generated prime (with high probability) is:", p)

    return(p)




# referred to: https://medium.com/@prudywsh/how-to-generate-big-prime-numbers-miller-rabin-49e6e6af32fb, code was written on my own
def generate_n_bit_number(bit_size):

    p = getrandbits(bit_size)
    mask_bit_string = 1 << (bit_size - 1) | 1  # number of the form 1000..0001, of len = bit_size
    p = p | mask_bit_string  # to make sure most significant bit is 1 (so it's actually an n-bit prime), least significant bit is 1 (so its odd)

    return(p)



if __name__ == "__main__":

    #print(pow(7,90, 5))
    #print(square_and_multiply(7,90, 5))

    #print(extended_euclidean(31,-45))
    #print(extended_euclidean(1432, 123211))

    print(generate_n_bit_prime(300))

'''
    test_cases_for_rabin_miller = [221]

    for i in range(100):
        print(rabin_miller(221)) # 221 is known to be composite, 13*17 = 221



    for test_case in test_cases_for_rabin_miller:
        print(rabin_miller(test_case))
'''
