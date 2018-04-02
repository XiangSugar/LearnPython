# -*- coding :utf-8 -*-
# This is about StringIO

from io import StringIO

f = StringIO()
f.write('Hello')
f.write(' ')
f.write('world!')
print(f.getvalue())  # getvalue() 用于获得写入后的 str

# 可以用 str 初始化 StringIO
f1 = StringIO('Hello!\nHi!\nGoodBye!')
while True:
    s = f1.readline()
    if s == '':
        break
    print(s.strip())