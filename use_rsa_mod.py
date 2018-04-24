# coding = utf-8

import rsa

key        = rsa.newkeys(2048)#生成随机秘钥
privateKey = key[1]#私钥
publicKey  = key[0]#公钥
message    = 'sanxi Now is better than never.'
print('Before encrypted:',message)

messagebyte_origin = message.encode()
print(messagebyte_origin)

cryptedMessage = rsa.encrypt(messagebyte_origin, publicKey)
print('After encrypted:\n',cryptedMessage)

messagebyte_decrypt = rsa.decrypt(cryptedMessage, privateKey)
print('The decrypt date byte:', messagebyte_decrypt)

message_decrypt = messagebyte_decrypt.decode()
print('After decrypted:', message_decrypt)