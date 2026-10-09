"""
迭代器:
    概述：自定义的类，重写 __iter__() 和 __next__() 方法，返回一个迭代器对象。
    处理大型数据
"""

for i in range(1,5,1):
    print(i)
print("--------------")

class MyIterator:
    #初始化属性，指定范围
    def __init__(self,start,end):
        self.current = start
        self.end = end

    #重写 __iter__() 方法，返回迭代器对象本身
    #人话：把数据传给next方法
    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration  #出现异常，迭代器结束
        value = self.current  #当前值value 1 2 3 4
        self.current += 1      #步长
        return value
    
for i in MyIterator(1,5):
        print(i)
print("--------------")

#通过next()函数获取迭代器的下一个值
it = MyIterator(1,5)
print(next(it))  #1
print(next(it))  #2
         