# 进程池（Process Pool）--------------------------
# 进程池可以创建多个进程
# 这些进程就相当于随时待命的士兵，准备随时指向任务（程序）
'''
import multiprocessing as mul

def f(x):
    print('process_name:{},process_id:{},result:{}'.format(mul.current_process().name,mul.current_process().pid,x**2))
    #return x**2

if __name__=='__main__':
    pool = mul.Pool(3)
    rel = pool.map(f,[1,2,3,4,5,6,7,8,9,10])

    # print(rel)
'''

# 上面是建立了5个进程的进程池，Pool 运行的每个进程都执行f() 函数
# 利用map() 函数，将f()函数作用到列表中的每个进程
# 这里的map() 函数和内置函数中的map()函数一样

# 共享资源-----------------------------------------

# 在前面提到过，我们应该尽量避免多进程共享资源
# 多进程共享资源必然会带来进程间相互竞争
# 这种竞争又会造成racecondition，我们的结果有可能被竞争的不确定性所影响
# 但如果需要，我们依然可以通过共享内存和Manager对象这么做

# 共享内存（shared memory）-----------
'''
import multiprocessing as mul

def f(n,a):
    n.value = 3.14
    a[0] = 5

num = mul.Value('d',0.0)
arr = mul.Array('i',range(10))

if __name__=='__main__':
    print(num.value,arr[:])
    p = mul.Process(target = f,args = (num,arr))
    p.start()
    p.join()
    print(num.value,arr[:])
    '''
    
# 这个共享内存。这里有主进程和创建的 p 进程，我们在主进程创建了两个值
# 并进行了初始化，一个是双精度的（d）,一个是数组，类型是（i）整数
# 在新建的进程中，我们对这两个对象的值做了修改，回到主进程
# 打印这两个对象的值，是被修改过。这说明在这两个进程间内存共享

# Manager--------------------------
# Manager类似于服务器于客户端之间的通信
# 我们用作一个进程作为服务器，建立Manager来真正存放资源
# 其他的进程可以通过参数传递或者根据地址来访问Manager，建立连接后，操作资源

import multiprocessing as mul

def f(n,a,l):
    n.value = 3.14
    a[0] = 5
    l.append('hello')

if __name__=='__main__':
    server = mul.Manager()
    num = server.Value('d',0.0)
    arr = server.Array('i',range(10))
    l = server.list()
    print(num.value,arr[:],l)
    p = mul.Process(target = f,args = (num,arr,l))
    p.start()
    p.join()
    print(num.value,arr[:],l)
