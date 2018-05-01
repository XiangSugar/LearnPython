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

def tcplink(sock, addr):
    print('accept new connection from %s: %s...' %(sock, addr))
    
    key        = rsa.newkeys(1024) #生成随机秘钥
    privateKey = key[1] #私钥
    publicKey  = key[0] #公钥
    n          = publicKey.n
    e          = publicKey.e
    str_n      = str(n)
    str_e      = str(e)

    sock.send(b'Welcome!')

    # 确保客户端已经打开之后才发送公钥
    start_data = sock.recv(BUFSIZE)
    if start_data.decode('utf-8') == 'start':
        sock.send(str_n.encode('utf-8'))
        time.sleep(1)
        sock.send(str_e.encode('utf-8'))
        time.sleep(1)


    while True:
        data = sock.recv(BUFSIZE)
        time.sleep(1)
        # 解密
        decrypt_data = rsa.decrypt(data, privateKey)
        
        print('Cilent: %s' % decrypt_data.decode())
        if not data or decrypt_data.decode() == 'exit':
            break

        d = 'Ser: Hello, ' + decrypt_data.decode()
        sock.send(d.encode('utf-8'))
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


