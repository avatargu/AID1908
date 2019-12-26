"""
IP地址
    ifconfig

    本地地址 :    "localhose","127.0.0.1" 　　　
    网络地址 :    "192.168.12.188"
    广播地址 :    "192.168.12.255"
    自动获取地址 : "0.0.0.0"

    注：网络地址每次不同

域名
    ping
    ping www.baidu.com
    "39.156.66.18"
    Ctrl + C

端口号
    MySQL 3306
"""

"""
客户端模拟程序：
telnet 127.0.0.1 8888
"""

import socket

print(dir(socket))

for item in dir(socket):
    print(item)
