"""
概述：
抽象类:有抽象方法的类
抽象方法:方法体是空实现(pass)
父类指定方法标准,子类实现具体的功能,这种叫抽象类.在py也可指接口,别的语言不一样
作用:抽象类一般充当父类,指定行业规范,子类实现具体功能
"""
class Ac:
    def cool_wind(self):
        pass
    def hot_wind(self):
        pass
    def swing(self):
        pass
class xiaomi(Ac):
    def cool_wind(self):
        print("小米技术")
    def hot_wind(self):
        print("小米技术")
    def swing(self):
        print("小米技术")
class geli(Ac):
    def cool_wind(self):
        print("格力技术")
    def hot_wind(self):
        print("格力技术")
    def swing(self):
        print("格力技术")

#创建对象
x=xiaomi()
b=geli()


#测试
x.cool_wind()
x.hot_wind()
x.swing()
b.swing()
b.cool_wind()