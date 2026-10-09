"""
多线程带参
在创建线程对象时，可以通过args参数传递位置参数，或者通过kwargs参数传递关键字参数。
args参数接受一个元组，包含要传递的位置参数。    
kwargs参数接受一个字典，包含要传递的关键字参数。
示例代码如下：    
"""




import multiprocessing
import time

def coding(name,count):
    for i in range(1,count+1):
        print(f"{name}正在写第 {i} 行代码.")
        time.sleep(0.1)



def music(name,count):
    for i in range(1,count+1):
        print(f"{name}正在听第 {i} 首音乐.")
        time.sleep(0.1)


#当前版本的多进程模块不支持在交互式环境中运行，所以需要在脚本中运行
#必须创建一个主函数，来创建和启动进程对象(不是固定语法，而是添加保护模块)
if __name__ == '__main__':
    # 创建进程对象
    p1 = multiprocessing.Process(target=coding, args=('Alice', 5))
    p2 = multiprocessing.Process(target=music,kwargs={'name':'Bob','count':5})

    # 启动进程
    p1.start()
    p2.start()