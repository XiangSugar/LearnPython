# -*- coding : utf-8 -*-
# 关于 type()
# 动态创建class对象

def fn(self, name='world'):  # 先定义函数
    print('Hello, %s' % name)

Hello = type('Hello', (object, ), dict(hello = fn)) # 创建 Hello class

h = Hello()
print(h.hello())
print(type(Hello))
print(type(h))