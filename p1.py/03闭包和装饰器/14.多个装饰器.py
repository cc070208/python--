"""
多个装饰器按从内到外装饰,表现为从上到下

"""

"""
1.登录
2.验证码
3.评论
"""

#登录
def check_login(fn_name):

    def fn_inner():
        print("校验登录")
        fn_name()
    return fn_inner

#验证码
def check_code(fn_name):

    def fn_inner():
        print("校验验证码")
        fn_name()
    return fn_inner


#评论
@check_login
@check_code
def comment():
    print("输入评论")



#测试
comment()