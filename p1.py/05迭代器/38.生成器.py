"""
生成器：基于一定规则生成数据的迭代器
目的：节省内存空间，提升性能
实现方式：
1.yield 关键字定义的函数  
2.推导式
"""
# my_list = [i for i in range(1,5)]
# my_generator = (i for i in range(1,5))
# print(type(my_list))  #<class 'list'>
# print(type(my_generator))  #<class 'generator'>
# for i in my_generator:
#     print(i)
# for i in my_list:
#     print(i)

#yield 关键字定义的函数
def my_generator():
    for i in range(1,5):
        yield i  #生成器函数，返回一个迭代器对象

my_gen = my_generator()
print(next(my_gen))
print('--------------')
for i in my_gen:
    print(i)