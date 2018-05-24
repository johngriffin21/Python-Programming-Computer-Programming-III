import threading
from time import sleep, ctime

def thread1(a,n):
    if n in a:
       print(a ,n ,"The required value {} is in the Array, so if theres a message after this, disregard it.\n".format(n))
    else:
       print(a,n,"The required value {} is not in the Array\n".format(n))

def main():
    print("Starting at",ctime())
    a = []
    for i in range(0,16):
        a.append(i)
    
    t2 = threading.Thread(target = thread1,kwargs = {"a":a[:4],"n":6})
    t3 = threading.Thread(target = thread1,kwargs = {"a":a[4:8],"n":6})
    t4 = threading.Thread(target = thread1,kwargs = {"a":a[8:12],"n":6})
    t9 = threading.Thread(target = thread1,kwargs = {"a":a[12:16],"n":6})
  
    t2.start()
    t3.start()
    t4.start()
    t9.start()
    
    t5 = threading.Thread(target = thread1,kwargs = {"a":a[:4],"n":20})
    t6 = threading.Thread(target = thread1,kwargs = {"a":a[4:8],"n":20})
    t7 = threading.Thread(target = thread1,kwargs = {"a":a[8:12],"n":20})
    t8 = threading.Thread(target = thread1,kwargs = {"a":a[12:16],"n":6})

    
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    
    sleep(5)
main()
