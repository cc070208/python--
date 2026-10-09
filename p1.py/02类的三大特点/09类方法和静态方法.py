""""
类方法：属于类的方法，通过类名.或对象名.的方法调用
        定义类方法要用装饰器@classmethod,第一个参数必须表示类对象
静态方法：类下对象公用的方法，调用方法同上
        定义该方法要用装饰器@staticmethod,参数可传不传
类对象就是指类，一用class
区别：1.参数要求
     2.要用类属性用类方法，否则用静态方法
     但一般使用静态方法，可以通过类名.调用属性
"""

class Student():
    school="黑马程序"
    @classmethod
    def show1(cls):
        print(f'cls:{cls}')
        print(cls.school)
        print("我是类方法")

    @staticmethod
    def show2():
        print(Student.school)
        print("我是静态方法")

s1=Student()
s1.show1()
s1.show2()
