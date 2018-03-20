# -*- coding : utf-8 -*-
# a function returns a function

def lazy_sum(*args):
    def calc_sum():
        ax = 0
        for x in args:
            ax = ax + x
        return ax
    return calc_sum

f1 = lazy_sum(1,2,3,4,5)
f2 = lazy_sum(1,2,3,4,5)
print('f1 = ', f1())
print('f2 = ', f2())
print('f1 = f2 : ', f1==f2)