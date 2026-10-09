"""
property() 函数的作用是将一个方法变成属性调用的形式。它可以让我们在访问一个方法时，不需要加括号，就像访问一个属性一样。
实现方式：
1.装饰器方式
2.类方式

装饰器用法：
    @property   修饰获取值的函数，即get类
    @属性名.setter  修饰设置值的函数，即set类


类属性用法：
    类属性名=property(获取值的函数,设置值的函数)
"""


class student:
    def __init__(self):
    
        self.__age = 18

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("年龄不能为负数")
        self.__age = value

class student2:
    def __init__(self):
        self.__age = 18

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if value < 0:
            raise ValueError("年龄不能为负数")
        self.__age = value

    age = property(get_age, set_age)#这一行依旧是类里面的




if __name__ == "__main__":
    # s = student()
    # print(s.age)  # 18
    # s.age = 20
    # print(s.age)  # 20
    # # s.age = -1  # ValueError: 年龄不能为负数

    s2 = student2()
    print(s2.age)  # 18
    s2.age = 20
    print(s2.age)  # 20
    # s2.age = -1  # ValueError: 年龄不能为负数