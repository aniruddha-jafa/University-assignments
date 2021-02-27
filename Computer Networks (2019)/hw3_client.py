import socket
import sys
import os
import random


'''
NOTE TO INSTRUCTOR:

Instead of taking user input manually, to simplify matters, I have written a function to randomly generate y1 and y2 self.
This should not affect the overall logic of the program.

'''


def toss_coin():
    choice = random.randint(0,1)
    if choice == 0:
        return "3"
    else:
        return "5"


def compute_49_digit_number():
    number= ""

    for i in range(49):
        digit = ""
        if i == 0: # don't let most significant bit be zero
            digit += str(random.randint(1,9))
        else:
            digit += str(random.randint(0,9))
        number += digit

    return number


def compute_z_y1_y2():
    a = compute_49_digit_number()
    x = toss_coin()
    y1 = a + x
    y2 = compute_49_digit_number()
    _50th_digit_y2 = str(random.sample([0,1,2,4,6,7,8,9],1)[0])
    y2 = a + _50th_digit_y2
    z = str(int(y1)*int(y2))

    return [z,y1,y2]




s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 31256           # Reserve a port for your service.

s.connect((host, port))
print("gethostname is:", socket.gethostbyname(host))
ack_message = s.recv(1024).decode()
print(ack_message)

numbers = compute_z_y1_y2()
z = numbers[0]
y1 = numbers[1]
y2 = numbers[2]
print("Length of z is", len(z))
print("z is:", z)


s.send(z.encode())
print("Have sent z to server")
#ack_message = s.recv(1024).decode()
#print("The following ack was received:", ack_message)


w = s.recv(1024).decode()
print("w sent by server has been received:", w)
#s.send("w_recevied".encode()) # send ack for w



s.send(y1.encode())

ack_message = s.recv(1024).decode()
print("Ack received")

s.send(y2.encode())

print("y1 and y2 sent")
print("y1 is:", y1)
print("y2 is", y2)

result = s.recv(1024).decode()
print("Result of the game is:", result)

last_tcp_segment = s.recv(1024)
print(last_tcp_segment.decode())


s.close
