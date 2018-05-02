# coding = utf-8

'''This is a server program based on TCP/IP communication.'''

import socket
import rsa
import threading
import time

HOST    = 'localhost'
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


def tcplink(sock, addr):
    print('accept new connection from %s: %s...' %(sock, addr))

    sock.send(b'Welcome!')

    # 接收公钥
    str_n = sock.recv(BUFSIZE).decode()
    if str_n:
        print('Got n...')
    str_e = sock.recv(BUFSIZE).decode()
    if str_e:
        print('Got e...')
    tn = int(str_n)
    te = int(str_e)
    publickey = Publickey(tn, te)
        
    while True:
        data = sock.recv(BUFSIZE)
        time.sleep(1)
        # 解密
        # decrypt_data = rsa.decrypt(data, privateKey)
        print('Cilent: %s' % data.decode())
        if not data or data.decode() == 'exit':
            break
        d = 'Server: Hello, ' + data.decode()
        crypt_data = rsa.encrypt(d.encode(), publickey)
        sock.send(crypt_data)
    sock.close()
    print('Connection from %s: %s is closed.' %(sock, addr))


tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

print('Waiting for connecting...')

while True:
    try:
        sock, addr = tcpSerSock.accept()
        # 创建一个新线程用于处理一个连接
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()
    except Exception as e:
        print('error: %s' % e)


