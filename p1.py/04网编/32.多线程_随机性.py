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
    #休眠
    time.sleep(0.2)
    #获取当前线程对象
    current_thread = threading.current_thread()
    print(current_thread)

if __name__ == "__main__":
    #创建线程对象
    for i in range(1,5):
        t = threading.Thread(target=print_infor)
        t.start()
