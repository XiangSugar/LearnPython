# coding = utf-8

'''This is a cilent program to test the comunication which is encrypted'''

import rsa
import socket

HOST    = '127.0.0.1'
PORT    = 9997
BUFSIZE = 2048
ADDR    = (HOST, PORT)

class Publickey(object):
    # def __ini__(self, tn, te):
    #     self.__tn = tn
    #     self.__te = te
    
    # def n(self):
    #     return tn
    # def e(self):
    #     return te
    __slots__ = ('n', 'e')

    def __init__(self, tn, te):
        self.n = tn
        self.e = te

tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
tcpCliSock.connect(ADDR)

# 接收欢迎消息:
print(tcpCliSock.recv(BUFSIZE).decode('utf-8'))

tcpCliSock.send(b'start')

# 接收公钥
str_n     = tcpCliSock.recv(BUFSIZE).decode()
if str_n:
    print('Got n...')
str_e     = tcpCliSock.recv(BUFSIZE).decode()
if str_e:
    print('Got e...')
tn = int(str_n)
te = int(str_e)
publickey = Publickey(tn, te)

while True:
    try:
        data = input('>')
        byte_data = data.encode()
        crypted_data = rsa.encrypt(byte_data, publickey)
        tcpCliSock.send(crypted_data)
        if data == 'exit':
            break

        print(tcpCliSock.recv(BUFSIZE).decode('utf-8'))
        
    except Exception as e:
        print('Error: %s' % e)

tcpCliSock.close()