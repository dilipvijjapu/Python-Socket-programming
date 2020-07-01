
from threading import *



queue=[]
queue1=[]
lock=Lock()

class producer1(Thread):
    def run(self):
        global queue

        lock.acquire()
        for i in range(13,19):
                  queue.append(i)
        print("produced required product")
        lock.release()

class producer2(Thread):
    def run(self):
        global queue1

        lock.acquire()
        for i in range(19,25):
                    queue1.append(i)
        print("produced product")
        lock.release()


class consumer1(Thread):
    def run(self):
        global queue

        lock.acquire()
        if not queue:
                print("nothing in queue but consumer will try")
        for i in range(5):
                  print("consumer 1 counsumed",queue.pop(0))
        lock.release()


class consumer2(Thread):
    def run(self):
        global queue1

        lock.acquire()
        if not queue1:
                print("nothing in queue1 but consumer will try")
        for i in range(5):
                print("consumer2 consumed",queue1.pop(0))
        lock.release()


p1=producer1()
p2=producer2()
c1=consumer1()
c2=consumer2()
p1.start()
c1.start()
p1.join()
c1.join()
p2.start()
c2.start()
p2.join()
c2.join()


