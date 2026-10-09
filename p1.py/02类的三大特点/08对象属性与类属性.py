""""
属性:名词，描述类的
    对象属性：定义到init魔法方法类的属性，每个对象都有自己的内容
            通过对象名.的方法调用
    类属性：定义到类中，函数外的变量，所有对象共用的
           通过类名.方法调用和对象名.方法调用，一般用类名
"""
class Student():
    teacher_name="水镜"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return '姓名:%s,年龄:%d'%(self.name,self.age)
    
s1=Student('小明',10)
s2=Student('王',14)
print(s1)
print(s2)