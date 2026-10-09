#定义类
class Car:
    #属性
    #魔法方法，特点；自动调用
    # __init__()作用：初始化对象
    #无参类
    """def __init__(self):
        self.color="黑色"
        self.number="4"
     """
    #有参类
    def __init__(self,color,number):
        self.color=color
        self.number=number
    #__str__():返回属性
    def __str__(self):
        return f'颜色：{self.color},数量：{self.number}'
    #del函数，可手动调用，在手动调用处执行，不手动调用将会在程序结束后自动调用,需给出提示，表示删除对象
    #del函数删除的是对象整体，而非单独的对象属性
    #对象好像也没方法？不对，对象有方法 即类外调用的方法
    def __del__(self):
        print
        
    #方法
    def run(self):
        print(f'{self}会去跑')
    def show(self):
        print(f'颜色：{self.color},数量：{self.number}')
    #类内调用方法；self.方法名（）
    def work(self):
        self.run()
#创建对像 对象是类的具体代表，即类是抽象概念，属性与方法封装。对象是实际物，是类的具体实现
c1 = Car('red','4')
c2 = Car('黑色','4')
#类外方法调用；对象名.方法ps:类外设置属性是对应对象独有的，也就是其他对象想要有该属性得重新设置属性
#类外访问方法
c1.run()
#类外属性设置
c1.color="red"
c1.number="1"
#类外访问属性
print(f'颜色：{c1.color}，数量；{c1.number}')
#魔法方法测试
print(c1)