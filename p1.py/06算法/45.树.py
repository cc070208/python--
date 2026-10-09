"""
深度优先：快速找到搜索路径
广度优先：快速找到最短路径
"""





#1.定义node类，二叉树节点
import queue
from typing import Any


class Node(object):
    """节点类"""
    def __init__(self,item) -> None:
        self.item: Any=item
        self.lchild=None #左节点
        self.rchild=None #右节点

#2.定义BinaryTree类，二叉树
class BinaryTree(object):
    def __init__(self,node=None) -> None:
        self.root=node


    def add(self,item) -> None:
        #1.封装item为节点
        new_node: Node=Node(item)
        #root为空直接当前为root
        if self.root==None:
            self.root: Node=new_node
            return
        
        #root不为空
        queue = [self.root]
        while queue:
            #每次循环cur会到下一个节点，实现遍历
            #pop删除最后一个元素，并返回
            cur_node = queue.pop(0)
            #检测左节点
            if cur_node.lchild is None:
                cur_node.lchild = new_node
                return
            else:
                #将非空左节点加入遍历队列
                queue.append(cur_node.lchild)
            #检测右节点
            if cur_node.rchild is None:
                cur_node.rchild = new_node
                return
            else:
                #将非空右节点加入遍历队列，而非添加进入树
                queue.append(cur_node.rchild)

        

    def breadth(self) -> None:
        if self.root is None:
            return []
        #遍历结果
        result = []
        #遍历入口
        queue = [self.root]
        
        while queue:
            node = queue.pop(0)  # 取出队首节点
            result.append(node.item)  # 访问当前节点
            
            # 左右子节点入队
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)
        
        return result



    def preorder(self,root) -> None:#先序(根左右)
        if root is not None:
            print(root.item,end='')
            self.preorder(root.lchild)
            #右节点
            self.preorder(root.rchild)



    def inorder(self,root) -> None:#中序(左根
        if root is not None:
            self.inorder(root.lchild)
            print(root.item,end='')
            #右节点
            self.inorder(root.rchild)
    def postorder(self,root) -> None:#后序
     if root is not None:
                self.postorder(root.lchild)
                #右节点
                self.postorder(root.rchild)
                print(root.item,end='')
