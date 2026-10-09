"""
问题：累加次数不够
产生原因：多线程中，多个线程同时对共享变量进行操作，互相抢占资源执行
解决方案：使用线程锁（Lock）来保证同一时间只有一个线程对共享变量进行操作，从而避免数据竞争问题。
ps：开那出现死锁和锁不住问题
死锁：当两个线程都在等待对方释放锁时，就会发生死锁。此时，两个线程都无法继续执行，程序会陷入无限等待状态。
锁不住：当一个线程在持有锁的情况下，另一个线程尝试
锁只能用一把
"""

import threading
g_num = 0

# 创建锁对象
mutex = threading.Lock()
#创建锁对象
def fun1():
    global g_num
    mutex.acquire()  # 上锁
    for i in range(1000000):
        g_num += 1
    print(f'fun1:{g_num}')
    mutex.release()  # 解锁

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
   
