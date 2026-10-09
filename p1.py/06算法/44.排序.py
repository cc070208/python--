"""
冒泡排序:要点:1.比较总轮数:   list长度-1
             2.每轮比较轮数： list长度-1-轮数索引
             3.和谁比较：     j和j+1
        扩展：外循环-1:减少比较次数
             内循环-1:防止越界
             内循坏-i:减少比较
"""

"""
选择排序要点:1.比较轮数: n-1    
            2.每轮比较数:i+1,n
            3.和谁比较:i和min_index

"""
from platform import java_ver


def bubble_sort(my_list):
    n=len(my_list)
    #控制外循环次数 
    for i in range(n-1):
        #每轮比较次数
        for j in range (n-1-i):
            #按从小到大排序
            if my_list[j]>my_list[j+1]:
                #交换
                my_list[j],my_list[j+1]=my_list[j+1],my_list[j]
    return my_list


def select_sort(my_list):
    n=len(my_list)
    for i in range(0,n-1):
        #假设最小值的下标
        min_index=i
        #内层循坏
        for j in range(i+1,n):
            #进行比较
            if my_list[j]<my_list[min_index]:
                #此处是交换下表
                min_index=j
        #交换
        if min_index!=i:
            my_list[min_index],my_list[i]=my_list[i],my_list[min_index]




if __name__=='__main__':
    # my_list=[1,5,7,4,6,1,7,8]
    # list=bubble_sort(my_list)
    # print(list)
    my_list2=[2,5,9,7,3]
    select_sort(my_list2)
    print(my_list2)
