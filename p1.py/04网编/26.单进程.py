def fun_c():
    for i in range(5):
        print("helloworld")


def fun_b():
    for i in range(5):
        print("hello")



#单进程：严格从上到下执行代码，上一行结束才能执行下一行
fun_b()
print("-"*20)
fun_c()