from threading import Thread, Condition #Condition is far more elegant to use(in my humble opinion)
import time
import random

queue = []
MAX_NO = 10
condition = Condition()

class ProducerThread(Thread):
    def run(self):
        nums = list(range(5))           #This will create a list containing[0, 1, 2, 3, 4]
        global queue 
        while True:                     #A while loop to go through the Producer Thread
            condition.acquire()         #The old code selected a number from the list, no point in doing so
            if len(queue)==MAX_NO:
                print("The Queue is in fact full, now the producer is waiting") 
                condition.wait()
                print("There is now a space availible, the consumer now notifies producer")#This solves the old problem because we now wait until the queue is free.
            num = random.choice(nums)
            queue.append(num)
            print("We have Produced",num)
            condition.notify()
            condition.release()
            time.sleep(random.random())  #This is a far more logical way to solve the problem
        
class ConsumerThread(Thread):          
    def run(self):
        global queue
        while True:                     #A while loop to go through the Consumer Thread
            condition.acquire()
            if not queue:
                print("There's nothing in the queue, consumer is now waiting") #The queue is full so we must now wait until it is free so the producer can add something to the queue.
                condition.wait()
                print("Now the producer added something to the Queue") #Problem is solved by the condition.wait()
            num = queue.pop(0)
            print("We have Consumed", num)
            condition.release()                                         #We now release the thread 
            time.sleep(random.random())                                 #Invoke a random sleep time to allow the user to analyze results.


ProducerThread().start()
ConsumerThread().start()
