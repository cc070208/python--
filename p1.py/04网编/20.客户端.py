""""
客户端开发流程：
1.创建socket对象
2.连接到服务端 指定服务端的ip地址和端口号
3.接收服务端发送的数据并打印
4.发送数据给服务端
5.关闭socket对象

ps:客户端和服务端通过字节流(bytes)进行通信，发送和接收的数据都必须是字节流类型。
    解释：你和异地朋友通话，二者交互实际是通过两部手机进行的，通话内容就是字节流数据。  
 

"""



#导报
import socket

# 1.创建socket对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2.连接到服务端 指定服务端的ip地址和端口号
client_socket.connect(('192.168.10.11', 10086))
# 3.接收服务端发送的数据并打印
data = client_socket.recv(1024).decode('utf-8')
print(f'服务端说：{data}')
# 4.发送数据给服务端
client_socket.send(b'hello')
# 5.关闭socket对象
client_socket.close()