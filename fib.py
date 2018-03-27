# -*- coding : utf-8 -*-

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b   # print(b)
        a, b = b, a + b
        n = n + 1
    return 'Done'

g = fib(6) # 定义一个generator对象

while True: # 异常处理
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break