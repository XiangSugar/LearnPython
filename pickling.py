# -*- coding : utf-8 -*-
# 关于序列化

import pickle
import json

d1 = dict(name = 'Bob', age = 20, score = 90)
d2 = dict(name = 'Suxiang', age = 22, score = 88)

# 序列化对象 d1 为一个 bytes
pickle_d1 = pickle.dumps(d1)
# 打印出序列化之后的内容
print(pickle_d1)

f1 = open('/Users/Suxiang/Python/dump.txt', 'wb')
f2 = open('/Users/Suxiang/Python/dump2.txt', 'wb')
f3 = open('/Users/Suxiang/Python/dump2.txt', 'rb')
f4 = open('/Users/Suxiang/Python/dump2.txt', 'rb')

# 将序列化之后的 bytes 写入文件 dump.txt 中
f1.write(pickle_d1)
# 将 d1 反序列化
D1 = pickle.loads(pickle_d1)
f1.close()

print('\n')
# 输出反序列化后的对象
print(D1)
print('\n')

# 直接将 d2 序列化之后写入一个 file-like Object (保存在 dump2.txt 中)
pickle.dump(d2, f2)
f2.close()

# 读取 d2 序列化之后的 bytes
print(f3.read())
f3.close()

# 反序列化为对象 D3
D3 = pickle.load(f4)
f4.close()

print('\n')
print(D3)