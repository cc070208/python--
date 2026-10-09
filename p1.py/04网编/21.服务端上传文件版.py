""""
服务端开发流程：
1.创建socket对象
2.绑定ip地址和端口号    
3.设置最大接听数
4.等待客户端连接
5.读取客户端发送的数据(文件)
6.读取文件储存到指定文件中
7.关闭socket对象   
"""


#导报
import socket


# 1.创建socket对象
sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sever_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)     
  
# 2.绑定ip地址和端口号  
sever_socket.bind(('192.168.10.10', 40000))


# 3.设置最大接听数
sever_socket.listen(5)
print('服务器已启动，等待客户端连接...')


# 4.等待客户端连接
conn,addr = sever_socket.accept()
print(f'客户端{addr}已连接')





# 5.读取客户端发送的数据(文件)
 #5.3将读取的数据写入到文件中

with open('./04网编/data/my.txt','ab') as dest_f:  # 以二进制追加模式打开文件
    #5.1循环读取数据
    while True:
         #5.2每次读取1024字节数据
        data = conn.recv(1024)  # 接收数据必须是字节流类型
        if not data:
            break
        dest_f.write(data)  # 将读取的数据写入到文件中
print('文件接收完成')
# 7.关闭socket对象
conn.close()
  