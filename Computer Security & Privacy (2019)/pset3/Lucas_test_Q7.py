from math import gcd

def get_list_of_coprime_numbers(p): # p,original number
    list_of_coprime_numbers = []

    for i in range(2,p):
        if gcd(i,p) == 1:
            list_of_coprime_numbers.append(i)

    return(list_of_coprime_numbers)



def get_list_of_factors(m): # m is supposed to be p-1
    list_of_factors = []

    for i in range(2, int(m**(0.5)+ 1)):

        if m%i == 0:
            list_of_factors.append(i)
            list_of_factors.append(m//i)

    return(list_of_factors)


def find_a_primitive_root(p):

    list_of_factors = get_list_of_factors(p-1)

    #print("factors:", list_of_factors)

    primitive_roots = []

    for g in range(2, p): # check 2.... p-1
        is_primitive_root = True

        for q in list_of_factors:
            power = int((p-1)/q)

            #print (pow(g, power,p),g,power,p)
            if  pow(g,power,p) == 1:
                is_primitive_root = False


        if is_primitive_root == True:
            primitive_roots.append(g)

    return(primitive_roots)


if __name__ == "__main__":

    n = 761
    print("\n Primitive roots are:", find_a_primitive_root(761))

    print(get_list_of_factors(20))

    #print(get_list_of_factors(760))
