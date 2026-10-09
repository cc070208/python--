"""
nonlocal:py内置函数，可实现内部函数修改外部函数的变量
"""

#创建函数
def outer():                            
    a=100
    def inner():
        nonlocal a      
        a=a+1
        print(f'a:{a}')
    return inner

inner=outer() #按理说这一步完成outer调用直接弹出栈了，只剩下inner部分，但可能nonlocal保存变量到另一空间
inner()

