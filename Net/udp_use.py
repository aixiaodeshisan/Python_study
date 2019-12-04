#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@文件    :udp_use.py
@说明    :udp发送传输
@时间    :2019/11/28 21:04:58
@作者    :MrShiSan
@版本    :1.0
'''

from socket import *
import os


def send_msg(ip,port):
    print("1.创建udp socket")
    udp_socket = socket(AF_INET, SOCK_DGRAM)

    print("2.准备接收方地址")
    addr = (ip, port)

    print("3.从键盘获取数据")
    send_data = input("请输入需要发送的数据")

    print("4.发送数据到指定的电脑上的指定程序进程中")
    udp_socket.sendto(send_data.encode('utf-8'), addr)

    print("5.关闭套接字")
    udp_socket.close()
    pass

def recv_msg():
    print("1.创建udp socket")
    udp_socket = socket(AF_INET, SOCK_DGRAM)

    print("2.绑定本地的相关信息，IP + Port")
    ip ='' #  ip地址和端口号，ip一般不用写，表示本机的任何一个ip
    port =int(input ("请输入端口号"))
    try:
        udp_socket.bind((ip,port))
    except udp_socket as identifier:
        print("绑定端口失败！")
        pass

    print("3. 等待接收对方发送的数据")
    recv_data = udp_socket.recvfrom(1024)

    print("4.显示接收到的数据")
    print(recv_data[0].decode('gbk'))

    print("5.关闭套接字")
    udp_socket.close()
    pass

def main_show():
    print('----------UDP网络聊天器----------')
    print('----------1.发送消息-------------')
    print('----------2.接收消息-------------')
    print('----------3.重设对方ip-----------')
    print('----------4.退   出--------------')
    pass

def main():
    main_show()

    opposite_ip = input("请输入对方ip")
    opposite_port = int(input("请输入对方端口"))
    print("正在与ip = %s,prot = %d的主机通信" % (opposite_ip,opposite_port))

    chose = input("请做出选择")
    while(chose != '4'):
        if(chose == '1'):
            send_msg(opposite_ip,opposite_port)
            chose = '0'
            pass
        elif(chose == '2'):
            recv_msg()
            chose = '0'
            pass
        elif(chose == '3'):
            opposite_ip = input("请输入对方ip")
            opposite_port = int(input("请输入对方端口"))
            print("正在与ip = %s,prot = %d的主机通信" % (opposite_ip,opposite_port))
            chose = '0'
            pass
        elif(chose == '4'):
            print("程序即将退出...")
            pass
        elif(chose == '0'):
            chose = input("请做出选择")
            pass
        else:
            print("选择不存在，请重新选择！")
            chose = input("请做出选择")
            pass
    pass


if __name__ == "__main__":
    main()
    pass