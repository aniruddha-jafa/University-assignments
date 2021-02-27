import socket
import sys
import os
import random
import threading

print("It takes a while to get listening...")

counter = 0
list_of_packets = []
port = 31256
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name


def tcp_sniffer():

    #------ code suggested by Vineet Reddy and Paul Kurian ------#
    command2 = "sudo tcpdump port " + str(port) + " -i lo0 -s 0 -n -e -x -vvv >> tcp_segments.txt"

    os.system(command2)



s.bind((host, port))        # Bind host to the port
s.listen()     # making backlog parameter optional

thread_2 = threading.Thread(target = tcp_sniffer)
thread_2.start()

max_times_connection_allowed = 5
number_of_connections_so_far = 0


while True:
    print("Listening for next connection...")


    conn, addr = s.accept()
    print('Connected by', addr)


    number_of_connections_so_far +=1

    conn.send('Thank you for connecting'.encode())
    # can't send it as string; throws error
    print("Thank you message sent")
    print('Receiving...')


    z = conn.recv(1024)

    z = z.decode()
    print("Decoded z is:", z)
    print('Length of data received is', len(z))
    print("Done receiving data")


    w  = str(random.sample([3,5],1)[0]) # a string
    conn.send(w.encode())
    print("The following w has been sent to client:", w)
    print("Waiting to recive y1 and y2")

    h1 = conn.recv(1024).decode() # number as a string
    print("What we received for y1 is:", h1)
    print("Length of what we received is:", len(h1))

    conn.send("y1 received".encode())

    h2 = conn.recv(1024).decode() # number as a string
    print("What we received for y2 is:", h2)
    print("Length of what we received is:", len(h2))


    if int(z) == int(h1)*int(h2):
        w1 = int(h1[-1]) # least significant bit of h1
        w2 = int(h2[-1])  # least significant bit of h2
        w_as_int = int(w)

        if w_as_int == w1 or w_as_int == w2:
            conn.send("You win!".encode())
            print("Have told client they won")
        else:
            conn.send("You lose :(".encode())
            print("Have told client they lost")

    else:
        print("Error:  z =/= h1*h2")

    print("\n")


    f = open("tcp_segments.txt", "r+")

    output = f.read().splitlines()
    output_as_string = ''.join(output)


    # method of searching for IPV4 to get starting index of last TCP segment suggested by Paul Kurian
    index_if_last_IPV4_message = output_as_string.rfind('IPv4')
    starting_index_of_last_TCP_segment = index_if_last_IPV4_message - 19
    last_TCP_segment = output_as_string[starting_index_of_last_TCP_segment:]
    print("last_TCP_segment is sent to client is", last_TCP_segment) #= output[-6] # get last segment

    print("\n")

    f.close()
    conn.send(last_TCP_segment.encode())


    conn.shutdown(socket.SHUT_WR)
    conn.close()
