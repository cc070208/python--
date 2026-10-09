"""
该文件用于管理学生信息，增删改查，保存信息等
"""
 
# studentCMS/studentcms.py 第5行
from student import Student    
#创建管理类
class StudentCMS(object):
    #定义魔法方法，创建属性"
    def __init__(self):
        #创建列表，保存信息,同时创建了学生对象，但并未像平时那样给其命名
        self.stu_list=[
            Student('刘','男',18,'123','6'),
            Student('关','男',15,'456','4'),
            Student('张','男',16,'789','6')
        ]
    #实现打印，显示管理系统页面
    def show(self):
        print('*'*23)
        print("学生管理系统")
        print("\t1.添加学生信息")
        print("\t2.删除学生信息")
        print("\t3.修改学生信息")
        print("\t4查询单个学生信息")
        print("\t5.查询所有学生信息")
        print("\t6.保存学生信息")
        print("\t0.退出系统")
        print()
        print('*'*23)

    #1.实现添加功能
    def add(self):
        #提示输入用户信息，接收
        name=input('输入姓名；')
        gender=input('请输入性别：')
        age=int(input('输入年龄：'))
        phone=input('输入手机号：')
        des=input('输入描述：')
        #上述信息打包成对象
        stu=Student(name,gender,age,phone,des)
        #加入studentcms类中
        self.stu_list.append(stu)
        #提示添加成功
        print('添加成功\n')


        

    #2.删除功能
    def delete(self):
        #输入删除名字
        del_name=input('输入删除名字：')
        #遍历list,找到该学生
        for stu in self.stu_list:
            if stu.name==del_name:  #使用类的属性一定要记得是对象名.属性
                self.stu_list.remove(stu)
                print(f'学生{del_name}删除成功')
                break
        print('该学生不存在，请重新输入')


    #3.修改功能
    def update(self):
         #输入修改名字
        upd_name=input('输入修改名字：')
        #遍历list,找到该学生，给已经创建的对象命名stu
        for stu in self.stu_list:
            if stu.name==upd_name:  #使用对象的属性一定要记得是对象名.属性
                stu.age=int(input('请输入年龄：'))
                stu.gender=input('请输入性别：')
                print(f'学生{upd_name}修改成功')
                break
        print('该学生不存在，请重新输入')


    #4.查询单个
    def search_one(self):
          #输入从查找名字
        ser_name=input('输入查找名字：')
        #遍历list,找到该学生
        for stu in self.stu_list:
            if stu.name==ser_name: 
                print(stu)
                break
        print('该学生不存在，请重新输入')


    #5.查询所有
    def search_all(self):
        #判断长度为0,如果为0，提示暂无信息，请添加后查询
        if not self.stu_list:
            print('暂无信息，请添加后查询')
        #如果不为0，输出信息
        else:
            for stu in self.stu_list:
                print(stu)
    #6.保存功能
    def save(self):
        pass
    
    #7.加载信息
    def load(self):
        pass

    #8.跑通以上功能
    def start(self):
        #8.1
        #8.2循环
        while True:
            #8.3
            #8.4打印界面
            self.show()
            #提示输入编号，接收
            num=input('请输入数字：')
            #根据数字实现不同功能
            if num =='1':
                #print("添加信息\n")
                self.add()
            elif num=='2': 
                #print("删除信息\n")
                self.delete()    
            elif num=='3':
                #print("修改信息\n")
                self.update()
            elif num=='4':
                #print("查询单个信息\n")
                self.search_one()
            elif num=='5':
                #print("查询所有信息\n")
                self.search_all()
            elif num=='6':
                print("保存信息\n")
                self.save()
            elif num=='0':
                result=input('您要选择退出吗 Y/N')
                if result.lower()=='y':
                    print("谢谢您的使用")
                    break
            else:
                print("输入有误，请重新输入\n")

