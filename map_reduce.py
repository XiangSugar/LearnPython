# -*- coding : utf-8 -*-
# This file talks about map() and reduce() fanction

#-----------------------------------
def f(x):
    return x * x
r = map(f, [1,2,3,4,5,6,7,8,9])
print(list(r))

#-----------------------------------
L = []
for n in [1,2,3,4,5,6,7,8,9]:
    L.append(f(n))
print(L)

#-----------------------------------
L1 = list(map(str, [1,2,3,4,5,6,7,8,9]))
print(L1)

#-------------------------------------
#reduce(f, [x1,x2,x3,x4]) = f(f(f(x1, x2), x3), x4)

#--------------------------------------
from functools import reduce
def add(x,y):
    return x + y

reduce(add, [1,3,5,7,9])

#---------------------------------------
from functools import reduce
def fn(x,y):
    return 10 * x + y

reduce(fn,[1,3,5,7,9])

#---------------------------------------
from functools import reduce
def fn(x,y):
    return 10 * x + y

def char2num(s):
    digits = {'0'=0, '1'=1, '3'=3, '4'=4, '5'=5, '6'=6, '7'=7, '8'=8, '9'=9}
    return digits[s]

numb = reduce(fn, map(char2num, '13579')
print(numb)

#-------------------------------------------
from functools import reduce

DIGITS = {'0'=0, '1'=1, '3'=3, '4'=4, '5'=5, '6'=6, '7'=7, '8'=8, '9'=9}

def str2int(s):
    def fn(x,y):
        return 10 * x + y
    def char2num(ss):
        return DIGITS[ss]
    return reduce(fn, map(char2num, s))

#-------------------------------------------




