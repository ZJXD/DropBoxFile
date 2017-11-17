# subprocess 以及常用的封装函数---------------------------------
# 当我们运行Python的时候，我们都是在创建并运行一个进程
# 正如我们在Linux进程基础中结束的那样，一个进程可以 fork 一个子进程，
# 并让这个子进程 exec 另外一个程序。
# 在Python中，我们通过标准库中的 subprocess 包来 fork 一个子进程

# subprocess 包中定义有数个创建子进程的函数，这些函数分别以不同的方式创建子进程
# 所有我们可以根据需要来从中选取一个使用。
# 另外这个包还提供了一些管理标准流（standard stream）和管道（pipe）工具
# 从而在进程间使用文本通信

# 使用subprocess包 中的函数创建子进程的时候要注意：
# （1）、在创建子进程后，父进程是否暂停，并等待子进程运行
# （2）、函数返回什么
# （3）、当returncode不为0时，父进程如何处理

'''
import subprocess

rc = subprocess.call(["shell","cd .."])    # 程序名shell和参数“cd .. ”放在一个表中传递
print(rc)

rc = subprocess.call("cd ..",shell = True) # 父进程等待子进程完成，返回退出信息
print(rc)
'''

# Popen() ----------------------------------------------------
# 实际上，我们上面的三个函数都是基于Popen()的封装（wrapper）
# 这些封装的目的在于让我们容易使用子进程。
# 当我们想要更个性化我们的需求的时候，就要转向Popen类，该类生成的对象用来代表子进程

'''
import subprocess

child = subprocess.Popen(["ping","www.baidu.com"])
child.wait()

print("parent process")
'''

# 默认是主程序不会自动等待子程序完成，要调用 wait() 方法，父进程才会等待
# child.poll()  检查子进程状态
# child.kill()  终止子进程
# child.send_signal()  向子进程发送信号
# child.terminate()  终止子进程


# 子进程的文本流控制-------------------------------

import subprocess
child1 = subprocess.Popen(["cmd","cd .."],stdout = subprocess.PIPE)
child2 = subprocess.Popen(["cmd","dir"],stdin = child1.stdout,stdout = subprocess.PIPE)
out = child2.communicate()

print(out)

# subprocess.PIPE 将多个子进程的输入和输出连接在一起，构成管道（pipe）
