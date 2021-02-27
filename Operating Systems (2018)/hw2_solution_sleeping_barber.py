from threading import Thread, Lock, BoundedSemaphore, Event
import time
import random

workday_over = False
# meant to indicate when the program ends, so we can trigger an exit() call. Basically an end_flag

number_of_waiting_room_seats = 3
# meant to serve as a comparison variable for waiting_customers;
# len(waiting_customers) <= number_of_waiting_room_seats must always hold

waiting_customers = []
# the list of customers needs to be shared by the two classes, Barber and Customer. Hence, we define it in the global scope.

access_waiting_seats = Lock()
# a mutex ock that controls whether or not the Barber or Customer can access the list 'waiting_customers'.

barber_asleep = True
# indicates whether or not the barber is asleep, which helps with 'if' statements

sleep_status_lock = Lock()
# a lock that controls access to the variable 'barber_asleep'. Why do we need a lock?
# Becasue both the barber and a customer can control whether or not the barber is asleep, which means the variable 'barber_asleep' is a shared resource.
# If there are no more customers, the barber can put itself to sleep; if a customer finds the barber asleep, it can wake the barber up
# Note that we haven't formally proved that a lock is necessary; although it can't hurt us, which is why it's there.

barber_sleep_event = Event()
# Why on earth do we need an Event() to manage sleep when we already have 'barber_asleep' and 'sleep_status_lock'?
# Well, Events help trigger blocking calls; without it, merely using the variable barber_asleep would not lead to nice print statments. This is
# becasue the While loop in the fucntion barber_is_working runs perpetually, which means we need a blocking call to hold off things
# For instance, if we merely had:
#
#       if barber_asleep == True:
#             print("Barber is asleep")
#
# This would mean "Barber is asleep" could be printed multiple times for each iteration of the While loop where the if-statement is true. This would not be pretty
#
# In summary: if clean print statements were not a problem, we could have left Event() out [to my best knowledge]



class Barber:

    def __init__(self, name):
        self.name = str(name)


    def open_shop(self):
        print("Barbershop is opening")
        print("Number of seats in waiting room is: {0} \n".format(number_of_waiting_room_seats) )
        barber_work_thread = Thread(target = self.barber_is_working)
        barber_work_thread.start()


    def sleep(self):
        global barber_asleep

        sleep_status_lock.acquire()
        barber_asleep = True
        sleep_status_lock.release()

        barber_sleep_event.wait(15)
        # barber_sleep_event.wait() blocks until a customer enters the shop and wakes the barber up
        # by doing barber_is_working.set() via the funciton wake_barber


    def cut_hair(self, current_customer):

        print("Sweeney Todd is cutting Customer {0}'s Hair ".format(current_customer.name))
        chaircount = 1

        for customer in waiting_customers:
            print("Customer {0} is waiting on chair {1}".format(customer.name, chaircount))
            chaircount += 1

        hair_cut_time = random.randint(1,10)
        time.sleep(hair_cut_time)
        print("Customer {0}'s haircut is complete \n".format(current_customer.name))


    # this is the primary function for Barber in this program
    def barber_is_working(self):

        # declare global variables so that we ca reference them within the function, which means that they turn into shared vairables, functionally speaking.
        global barber_asleep
        global waiting_customers

        while True:
            access_waiting_seats.acquire()

            if len(waiting_customers) > 0: # i.e. if customer is ready

                current_customer = waiting_customers[0]
                del waiting_customers[0]
                access_waiting_seats.release()


                barber_sleep_event.clear()
                # clear() sets thet flag of the Event to False.
                # This is needed so that 'barber_sleep_event.wait()' in the function barber.sleep actually blocks if there are no customers left.
                # If we didn't do a clear(), than the internal flag of barber_sleep_event would still be set to True, and barber_sleep_event.wait() would not block

                print("Customer {0} is sitting in the barber chair".format(current_customer.name))

                self.cut_hair(current_customer)


            else:
               if workday_over == True: # recall that workday_over is our end flag
                   print("The workday is over; Sweeney Todd is shutting the shop")
                   access_waiting_seats.release()
                   exit()
               else:
                   access_waiting_seats.release()
                   print("There are no customers. Sweeney todd is sleeping")
                   self.sleep()

class Customer:

    def __init__(self, name):
        self.name = str(name)

    def wake_barber(self):
        global barber_asleep

        # all this function needs to wake the barber up is access to shared variable barber_asleep, and the Event barber_sleep_event

        sleep_status_lock.acquire()
        barber_asleep = False
        # the function wake_barber is called only if barber_asleep is True. Hence, to wake up barber, set barber_asleep to False.
        sleep_status_lock.release()

        barber_sleep_event.set()
        # do barber_sleep_event.set() so that tha blocking call made by 'barber_sleep_event.wait()' in the function 'sleep()' in Class Barber is dealt with.

        print("Customer {0} woke up Sweeney Todd".format(self.name))

    # This is the primary function for customer in this program
    def enter_barber_shop(self):
        global barber_asleep         # define these global variables so that they are recognised in the local namespace of the function
        global waiting_customers

        print("Customer {0} attempting to enter barbershop".format(self.name))

        access_waiting_seats.acquire()

        if len(waiting_customers) < number_of_waiting_room_seats:

            if barber_asleep == True:
                # if barber is asleep, wake barber up, and add self to waiting_customers

                self.wake_barber()
                waiting_customers.append(self)
                access_waiting_seats.release()


            elif barber_asleep == False:
                # if barber is not asleep, this means that he is busy cutting someone else's hair

                waiting_customers.append(self)    # add self to waiting customers, and indicate to barber that you are ready
                print("Barber is busy. Customer {0} is waiting on chair {1}".format(self.name, len(waiting_customers)))
                access_waiting_seats.release()    # release lock from waiting_seats

        else:
            print("All seats are full; customer {0} has left the shop".format(self.name))
            access_waiting_seats.release() # release lock on waiting seats


if __name__ == "__main__":

    Sweeney_Todd = Barber("Sweeney Todd")
    trials = input("How many people should try to go to the barbershop? - ")
    Sweeney_Todd.open_shop()

    count  = 1
    for i in range(trials):
        x = random.randint(10,100)
        if x % 3 == 0:
			customer = Customer(count)
			customer.enter_barber_shop()
			count += 1
        time.sleep(1)

    workday_over = True
