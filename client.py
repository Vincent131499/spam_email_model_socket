# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     client
   Description :
   Author :       StephenLau
   date：          2019/6/1
-------------------------------------------------
   Change Activity:
                   2019/6/1:
-------------------------------------------------
"""
from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpClientSock = socket(AF_INET, SOCK_STREAM)
tcpClientSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpClientSock.send(bytes(data, 'utf-8'))
    data = tcpClientSock.recv(BUFSIZ)
    if not data:
        break
    print(str(data, encoding='utf-8'))

tcpClientSock.close()

