# -*- coding :utf-8 -*-

import json

class Student(object):
    def __init__(self, name, age, score):
        self.name  = name
        self.age   = age
        self.score = score
        
s = Student('Bob', 20, 88)

# 该隐函数把任意 class 的实例变为 dict
t = json.dumps(s, default=lambda obj: obj.__dict__)
print(t)

def dictstudent(d):
    return Student(d['name'], d['age'], d['score'])

print(json.loads(t, object_hook=dictstudent))