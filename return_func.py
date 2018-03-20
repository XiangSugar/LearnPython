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

#-------------------------------------
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i * i
        fs.append(f)
    return fs  # 相当于返回了三次 f 函数,分别存放在fs[0],fs[1],fs[2]当中，（但是并不是立即执行）

#利用 f1,f2,f3来取出fs当中的三个函数
f1, f2, f3 = count()
#执行f1,f2,f3并输出结果
print(f1(), f2(), f3())

#----------------------------------------
def cnt():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))  #f(i)立即执行，因此i的当前值被传入f(),但是g()函数不会立刻执行
    return fs

f_1, f_2, f_3= cnt()
print(f_1(), f_2(), f_3())