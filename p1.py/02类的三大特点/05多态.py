"""
多态：同一函数接受不同参数有不同效果
使用前提：
    1.有继承
    2.有方法重写
    3.要有父类引用指向子类
"""
class Aniaml():       #抽象类:有抽象方法的类
    def speak(self):  #抽象方法:方法体是空实现(pass)
        pass          #父类指定方法标准，子类实现具体的功能，这种叫抽象类，在py也可指接口，别的语言不一样
class Dog(Aniaml):
    def speak(self):  #方法重写了
        print("汪汪汪")
class Cat(Aniaml):
    def speak(self):
        print("喵喵喵")
def make_noise(an:Aniaml):      #这是父类引用指向子类 ，强调参数是子类对象
    """
    函数执行分析:这里其实是类外方法调用,an可以看作是一个待定的对象
    """
    an.speak()
class Car():
    def speak(self):
        print(5)
#创建对象
d=Dog()
c=Cat()
e=Car()
make_noise(d)
make_noise(c)
make_noise(e)