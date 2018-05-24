#A solution I wrote to the Sleeping-Barber problem

import random
import time
from threading import Lock,Event,Thread

CLIENTS = ["john","greg","max","pluto","mo","scooby-doo","bob","max"] #this is the list of Clients we will use
hold = Lock()                                                         #the lock i will use throughout the code
ARRIVAL_WAIT = 0.01                                                   #a wait time that i used to keep the customers entering inconsistent and realistic


class Work:
    clientsInShop = []

    def __init__(self, barber, Chairs):                   #Save the barber thread
        self.barber = barber
        self.numberOfSeats = Chairs

    def begin(self):
        print('Shop is now taking Clients.')
        readyThread = Thread(target=self.barberStarts)
        readyThread.start()                  #Here we start the thread barber starts so that the barber is ready to recieve any customers(clear) or alternitvely sleep(wait)

    def barberStarts(self):

        while True:
            hold.acquire()

            if len(self.clientsInShop) > 0:
                c = self.clientsInShop[0]
                del self.clientsInShop[0]
                hold.release()
                self.barber.startCutting(c)
            else:
                hold.release()
                print('No Clients in the shop at the moment, the barber will go to sleep.')
                barber.sleep()
                print('Barber woke up.')

    def customer_enters(self, client):
        hold.acquire()
        print('{} entered the shop'.format(client.name))

        if len(self.clientsInShop) == self.numberOfSeats:
            print('No availible chairs, so {} will come back later.'.format(client.name))
            hold.release()
        else:
            print('{} found a seat and is now waiting to get hair done.'.format(client.name))
            self.clientsInShop.append(i)
            hold.release()
            barber.wakebarber()


class Client:
    def __init__(self, name):
        self.name = name


class Barber:
    barberstarted = Event()

    def startCutting(self, client): # Here I Set barber as busy as he's started to cut hair
        self.barberstarted.clear()  # so we clear the event as the hair is for all intents and purposes cut
        print('{} is currently getting their hair done.'.format(client.name))
        time.sleep(ARRIVAL_WAIT * random.random()) #A wait time makes it more realistic
        print('{} is finished and will leave.'.format(client.name))

    def sleep(self):
        self.barberstarted.wait()         #Here we use .wait() to let the thread wait for the next customer

    def wakebarber(self):
        print('')
        self.barberstarted.set()        #Barber is now ready to cut hair



if __name__ == '__main__':

    clients = []
    for i in CLIENTS:
        clients.append(Client(i))                   #So we can use the name of the Client by adding it to the Client class

    barber = Barber()                               #Save Barber() class as the variable barber to use to set the chairs
    work = Work(barber, Chairs=10)                  #Here I set the chairs to ten and this is used throughout the work class
    work.begin()                                    #Initiate the whole process


    for i in clients:
        work.customer_enters(i)                   # New client enters the barbershop
        time.sleep(ARRIVAL_WAIT * random.random()) #A wait to make the timing more realistic
