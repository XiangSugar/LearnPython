# coding = utf-8

'''This is a cilent program based on TCP/IP communication.'''

import socket

HOST    = '127.0.0.1'
PORT    = 9997
BUFSIZE = 2048
ADDR    = (HOST, PORT)

# tcpCliSock = socket(AF_INET, SOCK_STREAM)
# tcpCliSock.connect(ADDR)

# while True:
#     try:
#         dataorigin = input('>')
#         data = dataorigin.encode('utf-8')
#         if not data:
#             break
#         tcpCliSock.send(data)
#         data = tcpCliSock.recv(BUFSIZE)
#         if not data:
#             break
#         print("Server: %s" % data)
#     except Exception as e:
#         print('Error: %s' % e)

# tcpCliSock.close()

tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
tcpCliSock.connect(ADDR)
# 接收欢迎消息:
print(tcpCliSock.recv(BUFSIZE).decode('utf-8'))
# for data in [b'Michael', b'Tracy', b'Sarah']:
#     # 发送数据:
#     tcpCliSock.send(data)
#     print(tcpCliSock.recv(BUFSIZE).decode('utf-8'))

# tcpCliSock.send(b'exit')
# tcpCliSock.close()
while True:
    try:
        data = input('>')
        
        tcpCliSock.send(data.encode('utf-8'))
        if data == 'exit':
            break

        print(tcpCliSock.recv(BUFSIZE).decode('utf-8'))
        
    except Exception as e:
        print('Error: %s' % e)

tcpCliSock.close()