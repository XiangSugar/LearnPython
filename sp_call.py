# -*- coding : utf-8 -*-

class Student(object):
    def __init__(self, name):
        self.name = name
    
    def __call__(self):
        print('My name is %s' % self.name)

s = Student('Xiang Su')
s()

print(callable(s))
print(callable(Student('Michael')))
print(callable([1,2,3]))
print(callable(max))
print(callable(None))
print(callable('str'))