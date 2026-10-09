"""
步骤：
1.导包
2.创建对象
3.自动线程
传参方式：元组
        字典
"""

import threading
import time

#1.定义对象
def  coding(name,count):
    for i in range (1,count+1):
        print(f"{name}正在写代码{i}")
        time.sleep(0.5)

def music(name,count):
    for i in range (1,count+1):
        print(f"{name}正在听音乐{i}")
        time.sleep(0.5)

#2.测试
if __name__ == "__main__":
    #创建线程对象
    t1 = threading.Thread(target=coding,args=("小明",5))
    t2 = threading.Thread(target=music,kwargs={"name":"小红","count":5})

    #2.1启动线程
    t1.start()
    t2.start()

    #等待线程结束
    t1.join()
    t2.join()