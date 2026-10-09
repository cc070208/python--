"""
链表
"""

from operator import truediv


class linkednode: #表示节点类，；类似结构体
    def __init__(self,item):
        self.item = item
        self.next = None

class linkedlist:
    def __init__(self,node=None):
        self.head=node  #头节点


#2.is_empty(self) 检查是否为空
#思路：判断head是否为空
   
    def is_empty(self):
    #方法1
    #     if self.head == None:
    #         return True
    #     else:
    #         return False
    

    #方法2：
        return self.head ==None


#3.length(self)  链表长度
    def length(self):
        cur = self.head
        count = 0
        while(cur!=None):
            count+=1
            cur = cur.next
        return count
        

# 4.travel(self) 遍历
    def travel(self):
        if self.is_empty():
            print("链表为空")
            return
        
        cur = self.head
        result = []  # 收集所有元素
        while(cur != None):
          print(cur.item)
          cur = cur.next

#5.add(self)    
    def add(self,item):
        node  = linkednode(item)
        node.next = self.head
        self.head = node 
       
#6.append(self) 尾部增加
    def append(self,item):
        node = linkednode(item)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while(cur.next!=None):
                cur = cur.next
            cur.next = node
        
#7.insert(self) 插入
    def insert(self,item,pos):
        length=self.length()
        if pos < 0 or pos > length:
            raise IndexError(f"插入位置 {pos} 超出范围 [0, {length}]")
        else:
            #首添加
            if pos==0:
                self.add(item)
                #尾部添加
            elif pos==length:
                self.append(item)
            else:
                #创建节点
                node = linkednode(item)
                #创建游动指针
                cur = self.head
                count = 0
                while(count<pos-1):
                    #要加入的前一位置，要插入5，则count为4
                    cur=cur.next
                    count+=1
                node.next=cur.next
                cur.next=node

#8.remove(self) 按值删除
    def remove(self,item):
        #创建游动指针
        cur=self.head
        #记录要删除节点的前驱节点
        pre=None
        #遍历
        while(cur!=None):
            if cur.item==item:
                #如果是头节点
                if cur==self.head:
                    #设置下一节点是头节点
                    self.head=cur.next
                #如果不是头节点，设置前一节点地址指向当前地址
                else:
                    pre.next=cur.next
                    cur.next=None 
                #当前结束
                return
            else:
                #未找到，此时游标后移动，前驱节点后裔
                pre=cur
                cur=cur.next

#search(self)   查找
    def search(self,item):
        #创建游标
        cur=self.head
        #遍历
        while(cur!=None):
            #找到该元素
            if cur.item==item:
                return True
            #该节点不是，则算下一个
            cur=cur.next
        #遍历完没有找到
        return False

    

if __name__=='__main__':
    a=linkednode(20)
    # print(a.item)
    # print(a.next)
    # print("-"*23)
    my_linkedlist = linkedlist(a)
    # print(f'data:{my_linkedlist.head.item}')
    # print(f'指针:{my_linkedlist.head.next}')
    # print(my_linkedlist.is_empty())
    # print(my_linkedlist.length())
    my_linkedlist.add(10)
    my_linkedlist.append(40)
    my_linkedlist.insert(30,2)
    my_linkedlist.remove(30)
    my_linkedlist.travel()
    print(my_linkedlist.search(30))