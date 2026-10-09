class Student:
    def __init__(self):
        self.current=100
    def run(self):
        print("跑步中")
        self.current-=0.5
    def eat(self):
        print("吃喝中")
        self.current+=0.5
    def __str__(self):
        return f'当前体重：{self.current}'
xm=Student()
xm.run()
xm.run()
xm.eat()
print(xm)