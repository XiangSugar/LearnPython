# -*- coding : utf-8 -*-
# This file talks about the decorator

def now():
    print('2018-3-20')
f = now
print(f())

#-------------------------------------------
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def Now():
    print('2018-3-20-15:00')

print(Now())

# ---------------------------------------
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            printf('%s %s()' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2018-9-1')

# -------------------------------------------------------------------------------------------
# 以上经过 decorator 装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：
# 因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，
# 否则，有些依赖函数签名的代码执行就会出错
# Python 内置的functools.wraps就是干这个事的，所以，一个完整的 decorator 的写法如下：
# -------------------------------------------------------------------------------------------
import functools

def log_1(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log_1('execute')
def now_1():
    print('2018-3-20 15:17')

print(now_1())

# 在装饰器的返回函数的定义之前加上  @functools.wraps(func)  即可
