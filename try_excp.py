# -*- coding : utf-8 -*-
# try...exception...

# 当捕获到错误后停止向下执行语句，会跳转到错误处理代码处执行
# 即 except 语句块
# 如果没有发生错误，则 except 语句不会执行
# 可以有多个 except 来捕获不同类型的错误
# 如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句
try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('No error!')
finally:  # 如果有 finally 则不管是否发生错误，都会执行完 finally 语句
    print('finally...')
print('END')


#------------------------------------------------------------------------
# Python 的错误其实也是 class，所有的错误类型都继承自BaseException，
# 所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也 “一网打尽”

# 第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类，
# 如果有错，也被第一个except给捕获了
try:
    foo()
except ValueError as e:
    print('ValueError!')
except UnicodeError as e:
    print('UnicodeError!')


#-----------------------------------------------------------------
# 跨越多层调用
# 不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了

def fo(s):
    return 10 / int(s)

def bar(s):
    return fo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error!: ', e)
    else:
        print('No error!')
    finally:
        print('finally...')
    
print(main())

#----------------------------------------------------
# err_logging.py
# Python 内置的logging模块可以非常容易地记录错误信息

import logging

def Fo(s):
    return 10 / int(s)

def Bar(s):
    return Fo(s) * 2

def main():
    try:
        Bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')