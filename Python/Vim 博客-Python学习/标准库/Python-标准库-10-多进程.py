'''
import os
import threading
import multiprocessing

# worker function
def worker(sign,lock):
    lock.acquire()
    print(sign,os.getpid())
    lock.release()

# Main
print('Main:',os.getpid())

# Multi-thread

lock = threading.Lock()
for i in range(5):
    thread = threading.Thread(target = worker,args = ('thread',lock))
    thread.start()
    record.append(thread)

for thread in record:
    thread.join()

# Multi-process
record = []
lock = multiprocessing.Lock()
for i in range(5):
    process = multiprocessing.Process(target = worker,args = ('process',lock))
    process.start()
    record.append(process)

for process in record:
    process.join()
'''

# pipe-------------------------------------
# Pipe 可以是单向的，也可以是双向的，建立的时候默认是双向的
# multiprocessing.Pipe(duplex=False),建立单向的
# 一个进程从PIPE一端输入对象，然后被另一端的进程接收
# 单通道只允许通道的一端进程输入，双向通道允许从两端输入

'''
import multiprocessing as mul

def proc1(pipe):
    pipe.send('hello')
    print('proc1 rec:',pipe.recv())

def proc2(pipe):
    print('proc2 rec:',pipe.recv())
    pipe.send('hello,too')

if __name__=='__main__':
    pipe = mul.Pipe()
    p1 = mul.Process(target = proc1,args = (pipe[0],))
    p2 = mul.Process(target = proc2,args = (pipe[1],))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
'''

# Queue-------------------------------------
# Queue 和 Pipe 类似，都是先进先出的结构。Queue 允许多个进程放入，多个进程取出
# Queue 使用 multiprocessing.Queue(maxsize)创建，maxsize 标识队列中可存放最达数量

import os
import multiprocessing
import time

def doChore():
    time.sleep(0.5)

# input worker
def inputQ(queue):
    info = str(os.getpid()) + '(put):' + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    queue.put(info)
    print(queue.qsize())

# output worker
def outputQ(queue,lock):
    info = queue.get()
    lock.acquire()
    print (str(os.getpid()) + '(get):' + info)
    # print (queue.qsize())
    # doChore()
    lock.release()

# Main

if __name__=='__main__':
    record1 = []
    record2 = []
    lock = multiprocessing.Lock()
    queue = multiprocessing.Queue(3)
    
    # input processes
    for i in range(10):
        process = multiprocessing.Process(target = inputQ,args = (queue,))
        process.start()
        record1.append(process)
        
    # output processes
    for i in range(10):
        process = multiprocessing.Process(target = outputQ,args = (queue,lock))
        process.start()
        record2.append(process)
        
    for p in record1:
        p.join()
        
    queue.close()
    
    for p in record2:
        p.join()
