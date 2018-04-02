# -*- coding：utf-8 -*-
# This is about BytesIO

# StringIO 只能操作 str 
# 操作二进制数据需要 BytesIO

from io import BytesIO

f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

# 注意： 写入的不是str，而是经过 utf-8 编码的 Bytes

# 可以用 bytes 初始化 BytesIO
f1 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f1.read())