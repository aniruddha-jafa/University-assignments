
from pset_4_helper_functions import*
import time

def read_file_for_ec_domain_params(file_name): # 4-4 (a):  Read a file of EC domain parameters
    file = open(file_name, "r")
    ec_params = file.readline().rstrip("\n")
    file.close()

    ec_params = ec_params.split(" ")

    p = int(ec_params[0])
    a = int(ec_params[1])
    b = int(ec_params[2])

    if are_ec_params_valid(p,a,b) == True:
        return([p,a,b])
    else:
        print("EC params are invalid i.e.  4a^3 + 27b^2 == 0  (mod p)")
        return(False)

def are_ec_params_valid(p, a, b):
    # check if 4a^3 + 27b^2 =/= 0  (mod p)
    if (4*square_and_multiply(a,3,p) + 27*square_and_multiply(b,2,p))%p != 0:
        return(True)

    else:
        return(False)


def check_if_point_belongs_to_ec(point, ec_params):
    # x and y coordinates

    if point == [-1,-1]:
        return(True)

    p = ec_params[0]
    a = ec_params[1]
    b = ec_params[2]

    x = point[0]%p
    y = point[1]%p

    if   (y**2)%p == ( (x**3) + (a*x) + b )%p:   # check if y^2 = x^3 + ax + b (mod p)
        return(True)
    else:
        print("y^2, RHS are:  ", (y**2)%p ,( (x**3)%p + (a*x)%p + b%p )%p )
        return(False)


def add_two_ec_points(point_1, point_2, ec_params):

    if len(point_1) != 2 or  len(point_2) !=2:
        print("Invalid point")

    #--->  first check for if points belong to EC
    if check_if_point_belongs_to_ec(point_1, ec_params) == False or check_if_point_belongs_to_ec(point_2, ec_params) == False:
        print("invlaid points. At least one doesn't lie on the specified EC")
        return(False)

    O_infty = [-1,-1]  # define point at infinity

    p = ec_params[0] # the modulo world we're in
    a = ec_params[1]

    x1, y1 = point_1[0]%p, point_1[1]%p
    x2, y2 = point_2[0]%p, point_2[1]%p


    # Case 1:  O + O = O
    if (point_1 == O_infty) and (point_1 == point_2):
        #print("case 1: both O")
        return(O_infty)

    # Case 2:  P + O = O + P = P
    elif (point_1 == O_infty and point_2 != O_infty) or  (point_1 != O_infty and point_2 == O_infty):
        #print("case 2: exactly one is O")
        if point_1 != O_infty:
            return(point_1)
        else:
            return(point_2)

    # Case 3: adding points with same x-coordinates and different or equal to zero y coordinates
    elif (x1== x2) and (y1 != y2 or y1 == y2 == 0):
        #print("case 3: same x-coordinates, and different or equal to zero y coordinates")
        return(O_infty)


    # Case 4: Not point doubling, points have differnt x-coordinates
    elif point_1 != point_2:
    #   print("case 4: different points, different x-coordinates, not O")

        slope = (   ((y2 - y1)%p) *  find_modular_inverse(x2-x1,p)  )%p  # lambda = (yQ - yP).(xQ - xP)^(-1) mod p
        x3 = ( (slope**2)%p - x1 - x2)%p  # xR =  lambda^2  -  xP -   xQ  mod p

        y3 = (  (slope*(x1 - x3))%p   - y1  )%p                    # yR = lamda(xP - xR)  - yP  mod p

        return([x3, y3])

    # Case 5: point doubling
    else:
        #print("case 5: point doubling")

        slope = (  (3*square_and_multiply(x1,2,p) +  a)*find_modular_inverse(2*y1, p) )%p  # lambda = (3x_p^(2)+ a ) (2*y_p)^(-1)  mod p

        print("slope is", slope)

        x3 = (square_and_multiply(slope, 2, p) -  2*x1)%p   # xR = lambda^2 - 2xP
        y3 =  (    slope*(x1 - x3)  - y1   )%p

        return([x3,y3])

def negate_ec_point(point):

    if point != [-1,-1]:
        return([point[0],-point[1]])

    else: # point at infinity
        return([-1,-1])

def subtract_two_ec_points(point_1, point_2, ec_params):
    return(add_two_ec_points(point_1, negate_ec_point(point_2)))

def point_multiplication_ec_point(k, point, ec_params):

    O_infty =  [-1, -1]

    if point == O_infty:
        return(O_infty)

    r = O_infty
    while k > 0:  # similar to square and multiply. least to most significant bit of k.
        if k%2 == 1:
            r = add_two_ec_points(r, point, ec_params)  #analoguous to r = r*a in square and multiply
        k = k//2
        point = add_two_ec_points(point, point, ec_params)  # analoguous to:  a = (a*a)%n in square and multiply

    return(r)

def check_if_y_values_exist_on_ec(x_coordinate, ec_params):

    p, a, b = ec_params[0], ec_params[1], ec_params[2]
    x = x_coordinate%p

    RHS_ec = (   (x**3)%p + (a*x)%p + b   )%p

    roots = find_square_roots_of_quadratic_residue(RHS_ec, p)
    print("roots (y values) are", roots, ", given x-coordinate:", x)

    return(roots)



if __name__ == "__main__":
    file_name = "elliptic_curve_parameters.txt"
    ec_params = read_file_for_ec_domain_params(file_name)
    print("EC parameters are:", ec_params, "\n")

    # * 4-4 (b): READ EC point from open stream
    point = input("Enter an EC point (in proper format) ")

    # * 4-4 (c): WRITE EC point to open stream
    print(point)



    """ IMPORTANT:   When running a test case, make sure all other test cases are commented out"""


    # test cases below:

    ''' # 0) test case to check y-coordinates of EC given x-coordinate
    check_if_y_values_exist_on_ec(5, ec_params)  # assume ec_params = [17,2,2]
    '''



    ''' # 1) test case to check point multiplication
    k_test_val = 2
    point = [3, 16]  # [5,1]
    point_multiplication_ec_point(k_test_val, point, ec_params)
    '''


    ''' # 2) a test case to check doubling
    print("mult", point_multiplication_ec_point(2, [3,1], ec_params))
    print("addition", add_two_ec_points([3,1], [3,1], ec_params))
    '''


    ''' # 3) test cases to test addition (by adding point to itself)
    # can also be used to cross-check point multiplication
    for i in range(2, 10):
        print(i, ")", point_multiplication_ec_point(i, point, ec_params))
    '''



    '''
    # 4) test case for bunch of point additions
    # code that asks for a pair of points, adss them, returns value, asks for two more points
    quit = False
    while not quit:
        # 4-4: READ EC point from open stream
        point_1 = input("Enter first EC point to add (in proper format): ").split(" ")
        point_2 = input("Enter second EC point to add (in proper format): ").split(" ")

        point_1 = list(map(int, point_1))
        point_2 = list(map(int, point_2))

        #print(point_1, point_2)

        #output added points here:
        print("The answer is: ", add_two_ec_points(point_1, point_2, ec_params))

        quit = bool(int(input('type "1" to quit, "0" to continue:')))
        print()
    '''
