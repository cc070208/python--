"""
该文件用于描述学生类,包括：姓名，性别，年龄，手机号，描述
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
    
#测试
if __name__=='__main__':
    s=Student('乔峰','男',41,165487,'爱喝酒')
    print(s)