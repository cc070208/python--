class herofighter():
    def power(self):
        return 60
class newfighter():
    def power(self):
        return 80
class enemy():
    def power(self):
        return 70
#创建平台函数
def object_play(hero,enemy):
    if hero.power()>enemy.power():
        print("我方获胜")
    else:
        print("敌方获胜")
#创建对象
a=herofighter()
b=enemy()
c=newfighter()
object_play(a,b)
object_play(c,b)
"""
封装               继承                                     多态
安全性，复用性      复用性                                   解耦(减少关联)
代码量增加          耦合性增强(模块间联系增强,不易修改) 

"""



