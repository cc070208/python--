""""
多线程特点：
1.多线程是随机执行，由cpu决定
2.默认情况下，主线程会等待子线程执行完毕后再结束
3.多线程之间共享全局变量，可能会出现数据安全问题，可用互斥锁解决
cpu调度策略：
1.时间片轮转调度策略：每个线程分配一个时间片，
2.抢占式调度策略：高优先级的线程可以抢占低优先级线程的执行时间
"""


my_list = []

import threading

def write_data():
    for i in range(5):
        my_list.append(i)
        print("写入数据：",i)
    print(f'write_data:{my_list}')

def read_data():
    print(f'read_data:{my_list}')

#测试
if __name__ == "__main__":
    #创建子线程
    t1 = threading.Thread(target=write_data)
    t2 = threading.Thread(target=read_data)
    t1.start()
    t2.start()
