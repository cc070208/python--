"""
问题：累加次数不够
产生原因：多线程中，多个线程同时对共享变量进行操作，互相抢占资源执行
解决方案：使用线程锁（Lock）来保证同一时间只有一个线程对共享变量进行操作，从而避免数据竞争问题。
"""

import threading
g_num = 0
#创建锁对象
def fun1():
    global g_num
    for i in range(1000000):
        g_num += 1
    print(f'fun1:{g_num}')

def fun2():
    global g_num
    for i in range(1000000):
        g_num += 1
    print(f'fun2:{g_num}')


if __name__ == "__main__":
    #创建子线程
    t1 = threading.Thread(target=fun1)
    t2 = threading.Thread(target=fun2)
    t1.start()
    t2.start()
   
