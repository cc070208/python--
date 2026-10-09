""""
    封装:将属性及方法写进类的操作
    私有属性或私有方法:封装进父类的方法和属性不继承给子类,父类独有
    实现私有方法:__属性(self)   __方法(self)
    获取私有属性方法：
    定义get__xx的方法.在父类写
    定义set__xx的方法修改
    ps:针对修改有两个情况1.在父类有set方法.则通过set修改了父类的私有属性,这里的修改并没有懂父类源代码.
    也就是我如果在使用set的情况下.重新创建父类对象,继续访问该属性.还是我们设置的初始父类私有属性
    即也只有一个对象的私有属性更改
    想要实现对源代码修改,也就是所有对象改变,则不能使用私有属性,
                       2.父类没有子类有set,实质是给子类设定新的私有属性,根据擦查找顺序父类优先,输出的还是父类属性
"""
class Master:
    def __init__(self):
        self.kongfu='古法配方'
        
    def make_cake(self):
        print(f'采用{self.kongfu}做煎饼')
class hm:
    def __init__(self):
        self.kongfu='hm配方'
    def make_cake(self):
        print(f'采用{self.kongfu}做煎饼')
#继承演示
class Prentice(Master,hm):
    #当子类属性或者方法与父类相同时，可以对其进行重写，此时优先调用子类方法及属性
    def __init__(self):
        self.kongfu='独创配方'
    #封装：某些属性，某些方法只在父类有，但子类不可对其进行重写
    #封装格式：__属性  __方法（）
        self.__money=10000
    #提供访问接口
    def get_money(self):
        return self.__money
    #提供设置接口
    def set_money(self,money):
        self.__money=money
    def make_cake(self):
        print(f'采用{self.kongfu}做煎饼')
#调用父类方法:类名.方法
    def Master_make_cake(self):
        Master.__init__(self)    #执行这行代码时，子类属性被替换成对应父类Master了，也就是独创被替换成古法 原理在这一步调用了父类属性
        Master.make_cake(self)
    def hm_make_cake(self):
        hm.__init__(self)        #执行这行代码时，子类属性被替换成对应父类hm了，也就是独创被替换成ai
        hm.make_cake(self)
class Tushun(Prentice):
    pass


tu=Tushun()
a=Prentice()
#封装演示私有属性的子类设置与获取
tu.set_money(100)
print(tu.get_money())
print(a.get_money())

