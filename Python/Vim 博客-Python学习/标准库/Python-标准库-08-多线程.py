# 面向过程--------------------------------------------
'''
import threading
import time
import os

def doChore():
    time.sleep(0.5)

def booth(tid):
    global i
    global lock
    while True:
        lock.acquire()         # 互斥锁，锁定
        if i != 0:
            i = i - 1
            print(tid,':now left:',i)
            doChore()
        else:
            print("Thread_id ",tid," No more tickets")
            os._exit(0)

        lock.release()         # 互斥锁，解锁
        doChore()

i = 100
lock = threading.Lock()

for k in range(10):
    new_thread = threading.Thread(target = booth,args = (k,))
    new_thread.start()
'''

# OOP（面向对象）----------------------------------------

import threading
import time
import os

def doChore():
    time.sleep(0.5)

class BoothThread(threading.Thread):
    def __init__(self,tid,monitor):
        self.tid = tid
        self.monitor = monitor
        threading.Thread.__init__(self)
    def run(self):
        while True:
            monitor['lock'].acquire()              # Lock
            if(monitor['tick'] != 0):
                monitor['tick'] = monitor['tick'] -1
                print(self.tid,':now left:',monitor['tick'])
                doChore()
            else:
                print("Thread_id:",self.tid," No more tickets")
                os._exit(0)                        # Exit the whole process
            monitor['lock'].release()              # Unblock
            doChore()

monitor = {'tick':100,'lock':threading.Lock()}

for k in range(10):
    new_thread = BoothThread(k,monitor)
    new_thread.start()


# 在这个里面用到的是字典 monitor ，作为可变数据对象，可以在多个线程间共享
# BoothThread 是继承自 threading.Thread ，构造函数里面对数据进行初始化
