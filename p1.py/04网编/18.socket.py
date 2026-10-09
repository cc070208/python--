"""
网络编程：又称网络通信，socket通信，即通信双方有自己的socket对象，
         数据在socket之间通过 数据报包(udp协议) 或 数据流(tcp协议) 进行传输。
    解释：你和异地朋友通话，二者交互实际是通过两部手机(双方手机就是socket对象)进行的，通话内容就是数据包或数据流。

"""

import socket

# 创建socket对象
#参1 address family地址族(ip地址种类)，AF_INET表示ipv4协议，AF_INET6表示ipv6协议
#参2 socket type套接字类型，SOCK_STREAM表示tcp协议，SOCK_DGRAM表示udp协议
#创建对象角度理解：第一个属性是ip地址种类，第二个属性是协议类型
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # tcp协议
print(s)