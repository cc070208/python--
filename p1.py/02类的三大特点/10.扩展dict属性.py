"""
__dict__:py的内置属性，把对象转换成字典
"""

# 1. 定义学生类 
class Student():
    #定义魔法方法，初始化学生信息
    def __init__(self,name,gender,age,phone,des):
        self.name=name
        self.gender=gender
        self.age=age
        self.phone=phone
        self.des=des
    
    def __str__(self):
        return f'姓名：{self.name},性别:{self.gender},年龄:{self.age}.手机号:{self.phone},描述:{self.des}'


#对象到字典
s1= Student('刘','男',18,'123','6'),
s2= Student('关','男',15,'456','4'),
s3= Student('张','男',16,'789','6')
my=s1.__dict__
stu_list=[s1,s2,s3]
print(my)