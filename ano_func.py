# -*- coding : utf-8 -*-
# The use of anonymous function

L = list(map(lambda x: x * x, [1,2,3,4,5,6]))
print(L)

# lambda x: x * x  等价于：
def f(x):
    return x * x

#-----------------------------------------
ff = lambda y: y * y
print(ff(5))

#------------------------------------------
def build(x, y):
    return lambda : x * x + y * y

#-------------------------------------------
L1 = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L1)