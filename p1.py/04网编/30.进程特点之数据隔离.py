"""
进程的特点：
    1.进程间的数据是隔离的
    子进程是父进程的副本，会将父进程的main外资源复制一份，详情看接下来的print函数
    即使父进程也不能读取子进程的数据
    本质解释：进程是cpu分配的资源单位，每个进程都有独立的栈
    2.默认情况，主进程会等待子进程结束后才会结束
    3.进程之间的通信需要使用进程间通信机制，如管道、消息队列、共享内存等

"""

#需求:创建公共容器my_list,一个进程向my_list中添加数据，另一个进程看是否能够读取
import multiprocessing
import time
#1.创建公共容器my_list
my_list = []

#2.一个进程向my_list中添加数据
def add_data():
    for i in range(1,6):
        my_list.append(i)
    print(f"add_data函数: {my_list}")


#3.另一个进程看是否能够读取
def read_data():
    time.sleep(1)
    print(f"read_data函数: {my_list}")


print("执行测试")
#4.测试
if __name__ == "__main__":
    #创建进程
    p1 = multiprocessing.Process(target=add_data)
    p2 = multiprocessing.Process(target=read_data)

    #启动进程
    p1.start()
    p2.start()

    #等待进程结束
    p1.join()
    p2.join()