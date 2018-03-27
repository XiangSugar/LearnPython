# -*- coding: utf-8 -*-
# __getitem__

class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n 是索引
            a, b = 1, 1
            for n in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n 是切片
            start = n.start  # 取出切片的起始值
            stop = n.stop    # 取出切片的终止值
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib()
print(f[5])
print(f[0:5])
print(f[:10])