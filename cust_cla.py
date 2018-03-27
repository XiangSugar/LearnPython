# -*- coding : utf-8 -*-
# 定制类

class Student(object):
    def __init__(self, name):
        self.name = name

   # __str__ 返回用户看到的字符串 为用户服务
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    
    # __repr__  为调试服务
    def __repr__(self):
        return 'Student object (name: %s)' % self.name
    #等价于
    #__repr__ = __str__  (因为函数内容是完全一样的)

print(Student('Michael'))
s = Student('Lisa')
s