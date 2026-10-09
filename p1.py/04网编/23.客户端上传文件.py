"""
需求：
1.创建客户端对象
2.链接到服务端端口
3.关联数据原，读取数据并打印
4.发送数据给服务端
5.关闭socket对象
"""

#导包
import socket   


#1.创建客户端对象
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  


#2.链接到服务端端口
client_socket.connect(('192.168.10.10',40000))


#3.关联数据原，读取数据并打印
#3.1关联数据源
with open('d:/绕口令.txt','rb') as src_f:  
    #3.2循环读取数据
    while True:
        #3.3每次读取1024字节数据
        data=src_f.read(1024)  
        if len(data)==0:  # 判断是否读取到数据，如果没有读取到数据，说明已经读取完了
            break
        #3.4打印数据
        client_socket.send(data)  # 发送数据必须是字节流类型

    
