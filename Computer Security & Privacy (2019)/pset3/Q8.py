from math import gcd
from random import randint



def get_list_of_coprime_numbers(n): # p,original number
    list_of_coprime_numbers = []


    for i in range(2,n):
        if gcd(i,n) == 1:
            list_of_coprime_numbers.append(i)

    return(list_of_coprime_numbers)

def find_s_and_t(e,d):
    num_as_binary = bin(e*d-1)[2:]
    index_of_first_nonzero_bit = None

    print(num_as_binary)

    s = 0
    for i in range(len(num_as_binary) - 1, -1, -1):  # last index of array to 0th index
        #print(i, num_as_binary[i])

        if num_as_binary[i] == "1":
            index_of_first_nonzero_bit =  i
            break

        else:
            s += 1

    #print(index_of_first_nonzero_bit)
    t = int(num_as_binary[:index_of_first_nonzero_bit+1],2)

    return([s,t])

def factor(n, e, d):

    s_and_t = find_s_and_t(e,d)
    s = s_and_t[0]
    t = s_and_t[1]

    print("s and t:", s_and_t )

    list_of_coprime_numbers = get_list_of_coprime_numbers(n)
    print("Coprime numbers", list_of_coprime_numbers)

    while True:

        index_of_rand_int = randint(0, len(list_of_coprime_numbers) - 1)

        a = list_of_coprime_numbers[index_of_rand_int]
        # print("a is:", a)
        b = pow(a,t,n)

        while pow(b,2,n) != 1:
            b = pow(b,2,n)

        if b % n != 1 and (b + 1) % n != 0:
            # do-while implimentation  b =/= +- 1 mod n
            # b = -1 mod n => n | b - (-1) i.e. n | b + 1  i.e.   (b + 1) % n == 0
            break

    print("b is:", b)
    print("a selected is:", a)

    p = gcd(b-1,n)
    q = int(n/p)

    return([p,q])


 if __name__ == "__main__":

    n =   55 # 1501
    e = 3  #  323
    d = 27  # 539

    #print(find_s_and_t(e,d))
    # print(get_list_of_coprime_numbers(16))

    #print(is_congruent_to_negative_1(54,55))
    print(factor(n,e,d))
