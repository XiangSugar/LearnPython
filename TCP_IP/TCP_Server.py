# coding = utf-8

'''This is a server program based on TCP/IP communication.'''

import socket
import threading
import time

HOST    = 'localhost'
PORT    = 9997
BUFSIZE = 2048
ADDR    = (HOST, PORT)

# tcpSerSock = socket(AF_INET, SOCK_STREAM)
# tcpSerSock.bind(ADDR)
# tcpSerSock.listen(5)

# while True:
#     try:
#         print('Waitting for connection...')
#         tcpCliSock, addr = tcpSerSock.accept()
#         print('Connected Client from: %s' % addr)

#         while True:
#             data = tcpCliSock.recv(BUFSIZE)
#             if not data:
#                 break
#             else:
#                 print('Cilent: %s' % data)
#             tcpCliSock.send('[%s] %s' %(ctime(), data))

#     except Exception as e:
#         print('error: %s' %e)

# tcpSerSock.close()

def tcplink(sock, addr):
    print('accept new connection from %s: %s...' %(sock, addr))
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(BUFSIZE)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        print('Cilent: %s' % data.decode('utf-8'))
        d = 'Hello' + data.decode('utf-8')
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


