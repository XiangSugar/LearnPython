# -*- coding : utf-8 -*-
# The use of filter()

def is_odd(n):
    return n % 2 == 1
L = list(filter(is_odd, [1,2,3,4,5,6,7]))
print(L)

#--------------------------------------------
def not_empty(s):
    return s and s.strip()

L1 = list(filter(not_empty, ['A', '', 'B', None, 'C', ' ']))
print(L1)

#----------------------------------------------
def is_palindrome(n):
    return str(n) == str(n)[::-1]

L2 = list(filter(is_palindrome, [123321, 7898, 3443,353,90]))
print(L2)
