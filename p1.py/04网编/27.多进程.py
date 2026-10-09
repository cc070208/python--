"""
多进程目的：
多任务的实现方式，提高效率，节省时间
并行：同时执行多个任务，适合CPU密集型任务，即多核cpu执行多任务
并发：交替执行多个任务，适合IO密集型任务，即单核cpu执行多任务
"""

"""
1.导包
2.创建进程对象
3.启动进程
"""


import multiprocessing
import time

def coding():
    for i in range(5):
        print("正在写代码...")
        time.sleep(0.1)



def music():
    for i in range(5):
        print("正在听音乐...")
        time.sleep(0.1)


#当前版本的多进程模块不支持在交互式环境中运行，所以需要在脚本中运行
#必须创建一个主函数，来创建和启动进程对象(不是固定语法，而是添加保护模块)
if __name__ == '__main__':
    # 创建进程对象
    p1 = multiprocessing.Process(target=coding)
    p2 = multiprocessing.Process(target=music)

    # 启动进程
    p1.start()
    p2.start()