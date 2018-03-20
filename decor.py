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

#----------------------------------------
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
