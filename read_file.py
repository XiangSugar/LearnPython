# -*- coding :utf-8 -*-
# IO programing

# 默认读取文本文件（utf-8编码的文本文件）

try:
    f = open('/Users/Suxiang/Python/README.md', 'r')
    print(f.read())
finally:
    if f:
        f.close()

#----------------------------------------------------
with open('/Users/Suxiang/Python/README.md', 'r') as f:
    #print(f.read())
    #print(f.read(5))
    for line in f.readlines():
        print(line.strip())  # 把末尾的'\n'删掉

#-----------------------------------
# 打开二进制文件， 用 'rb' 模式打开
with open('/Users/Suxiang/Downloads/iMacPro/FM.jpeg', 'rb') as ff:
    print(ff.read())

# 读取 GBK 编码的文件
# error 参数表示遇到错误后该如何处理
with open('/Users/Suxiang/Downloads/iMacPro/test.txt', 'r', encoding = 'gbk', errors = 'ignore') as fff:
    print(fff.read())