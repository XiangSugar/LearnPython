# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self):
        self.name = 'Xiang Su'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

s = Student()
print(s.name)
print(s.score)
print(s.age)