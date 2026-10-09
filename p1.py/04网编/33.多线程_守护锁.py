""""
多线程特点：
1.多线程是随机执行，由cpu决定
2.默认情况下，主线程会等待子线程执行完毕后再结束
3.多线程之间共享全局变量，可能会出现数据安全问题，可用互斥锁解决
cpu调度策略：
1.时间片轮转调度策略：每个线程分配一个时间片，
2.抢占式调度策略：高优先级的线程可以抢占低优先级线程的执行时间
"""

import threading
import time

def print_infor():
    for i in range(10):
        print("工作中")
        time.sleep(0.2)
  

if __name__ == "__main__":
    #创建子线程
    #通过设置daemon属性为True，将子线程设置为守护线程，主线程结束后，子线程也会结束
    t = threading.Thread(target=print_infor,daemon=True)
    t.start()
    time.sleep(1)
    #主线程结束
    print("主线程结束")