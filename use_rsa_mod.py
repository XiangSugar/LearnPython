# coding = utf-8

import rsa

key        = rsa.newkeys(1024)#生成随机秘钥
privateKey = key[1]#私钥
publicKey  = key[0]#公钥
n = privateKey.n
message    = 'sanxi Now is better than never.'
print('Before encrypted:',message)

messagebyte_origin = message.encode()
print(messagebyte_origin)

# 加密
cryptedMessage = rsa.encrypt(messagebyte_origin, publicKey)
# 打印加密后的信息（bytes）
print('After encrypted:\n',cryptedMessage)

# 解密
messagebyte_decrypt = rsa.decrypt(cryptedMessage, privateKey)
print('The decrypt date byte:', messagebyte_decrypt)

message_decrypt = messagebyte_decrypt.decode()
print('After decrypted:', message_decrypt)