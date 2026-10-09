"""
进程编号：
    概述：在设备上运行的程序(进程)，每个进程都有一个唯一的编号，叫进程编号。程序结束，该id就会被回收，重新分配给其他进程使用。
       目的：1.通过进程编号可以区分不同的进程，进行进程管理。
            2.杀死进程：通过进程编号可以杀死指定的进程，释放资源。
    格式：
        查看读当前进程的pid
            os模块的getpid()函数        get process id
            multiprocessing模块的current_process().pid属性、

        查看当前进程ppid: parent process id
            os模块的getppid()函数
            multiprocessing模块的current_process().ppid属性
"""



import multiprocessing,os
import time

def coding(name,count):
    for i in range(1,count+1):
        print(f"{name}正在写第 {i} 行代码.")
        time.sleep(0.1)
    print(f'p1进程的pid是{os.getpid()},ppid是{os.getppid()}')



def music(name,count):
    for i in range(1,count+1):
        print(f"{name}正在听第 {i} 首音乐.")
        time.sleep(0.1)
    print(f'p2进程的pid是{os.getpid()},ppid是{os.getppid()}')



if __name__ == '__main__':
    # 创建进程对象
    p1 = multiprocessing.Process(target=coding, args=('Alice', 5))
    p2 = multiprocessing.Process(target=music,kwargs={'name':'Bob','count':5})

    # 启动进程
    p1.start()
    p2.start()