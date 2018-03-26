# -*- coding: utf-8 -*-
# The use of __slots__

class Student(object):
    pass

s = Student()
s.name = 'Michael'
print(s.name)

def set_age(self, age):  #定义一个函数作为实例方法
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)  #给实例绑定一个方法
s.set_age(25)  #调用实例方法
print(s.age)  #测试结果

#给一个实例绑定的方法，对另一个实例不起作用
s2 = Student()
#s2.set_age(23)  #会失败

#----------------------------------------
def set_score(self, score):
    self.score = score

Student.set_score = set_score

s.set_score(100)
print(s.score)

s2.set_score(99)
print(s2.score)

#---------------------------------------
class Volunteer(object):
    __slots__ = ('name', 'gender', 'age')

v = Volunteer()
v.name = 'Jack'
v.gender = 'M'
v.score = 99  # 报错，因为限制了只能有三个属性，score不在这个行列

#__slots__ 定义的属性进仅对当前类的实例有作用，对继承的子类不起作用
class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 99  # 此处是可以的