""""
服务端开发流程：
1.创建socket对象
2.绑定ip地址和端口号    
3.设置最大接听数
4.等待客户端连接
5.发送数据给客户端
6. 接收客户端发送的数据
7.关闭socket对象   

ps:客户端和服务端通过字节流(bytes)进行通信，发送和接收的数据都必须是字节流类型。
    解释：你和异地朋友通话，二者交互实际是通过两部手机进行的，通话内容就是字节流数据。  


"""

#导报
import socket

# 1.创建socket对象
sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
# 2.绑定ip地址和端口号  
sever_socket.bind(('192.168.10.11', 10068))  
# 3.设置最大接听数
sever_socket.listen(5)
# 4.等待客户端连接
#conn是一个新的socket对象，相当于每个客户端的对应的专属通道，addr是客户端的ip地址和端口号

conn,addr = sever_socket.accept()

# 5.发送数据给客户端
conn.send(b'hello')  # 发送数据必须是字节流类型
# 6. 接收客户端发送的数据
data = conn.recv(1024).decode('utf-8')  # 接收数据必须是字节流类型，参数表示一次接收的最大字节数
print(f'收到来自{addr}的消息：{data}')
# 7.关闭socket对象,关闭对应客户而非服务端socket对象  
conn.close()

#8.扩展：设置端口复用，快速重启服务端
#参数1：socket.SOL_SOCKET 代表套接字级别
#参数2：socket.SO_REUSEADDR 代表允许重用本地地址和端口号
sever_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)