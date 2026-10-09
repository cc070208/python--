"""
1.装饰器只能有一个参数
2.需要多个参数的话,需要将装饰器作为内层函数
3.装饰器要写在被装饰的函数前面
"""

#需求：能够同时装饰加减法的装饰器


def logging(flag):
    def  my_computer(fn_nanme):


        def fn_inner(a,b):
            if flag=="+":
                print("正在进行加法计算")
            elif flag=="-":
                print("正在进行减法计算")
            return  fn_nanme(a,b)
        return  fn_inner
    return  my_computer


#优化版(感觉耦合性很强)
def  my_computer(fn_nanme):


    def fn_inner(a,b):
        if fn_nanme.__name__=='add':#这里指明我们传进来的是对象，所以才能调用对象方法
                print("正在进行加法计算")
        elif fn_nanme.__namme__=='sub':
                print("正在进行减法计算")
        return  fn_nanme(a,b)
    return  fn_inner
    


@logging('+')
def add(a,b):
    return a+b


@logging('-')
def sub(a,b):
    return a-b


#tast
print(add(1,2))

print(sub(2,1))
