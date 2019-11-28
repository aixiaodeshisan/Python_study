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


def send_msg():
    print("1.创建udp socket")
    udp_socket = socket(AF_INET, SOCK_DGRAM)

    print("2.准备接收方地址")
    addr = ("192.168.134.1", 8080)

    print("3.从键盘获取数据")
    send_data = input("请输入需要发送的数据")

    print("4.发送数据到指定的电脑上的指定程序进程中")
    udp_socket.sendto(send_data.encode('utf-8'), addr)

    print("5.关闭套接字")
    udp_socket.close()
    pass

def recv_msg():
    print("1.创建udp socket")

    print("2.")
    print("1.")
    print("1.")
    print("1.")
    print("1.")
    pass


def main():
    send_msg()
    pass


if __name__ == "__main__":
    main()
    pass