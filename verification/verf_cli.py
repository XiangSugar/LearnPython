# coding = utf-8

'''This is a cilent program to test the comunication which is encrypted'''

import rsa
import socket
import time

HOST    = '127.0.0.1'
PORT    = 9997
BUFSIZE = 2048
ADDR    = (HOST, PORT)

key        = rsa.newkeys(1024) #生成随机秘钥
privateKey = key[1] #私钥
publicKey  = key[0] #公钥
n          = publicKey.n
e          = publicKey.e
str_n      = str(n)
str_e      = str(e)

# 创建套接字
tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
tcpCliSock.connect(ADDR)

# 接收欢迎消息:
print(tcpCliSock.recv(BUFSIZE).decode('utf-8'))

tcpCliSock.send(str_n.encode('utf-8'))
time.sleep(1)
tcpCliSock.send(str_e.encode('utf-8'))
time.sleep(1)

# tcpCliSock.send(b'start')

while True:
    try:
        data = input('>')
        #byte_data = data.encode()
        #crypted_data = rsa.encrypt(byte_data, publickey)
        tcpCliSock.send(data.encode())
        if data == 'exit':
            break
        # 接收加密之后的数据
        encrypt_data = tcpCliSock.recv(BUFSIZE)
        print('encrypted_data: %s' % encrypt_data.decode('utf-8', errors='ignore'))
        decrypt_data = rsa.decrypt(encrypt_data, privateKey)
        print(decrypt_data.decode())
        
    except Exception as e:
        print('Error: %s' % e)

tcpCliSock.close()