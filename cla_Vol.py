# -*- coding: utf-8 -*-
# 为了统计志愿者人数，可以给 Volunteer 类增加一个类属性，每创建一个实例，该属性自动增加

class Volunteer(object):
    count = 0
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        Volunteer.count = Volunteer.count + 1

if Volunteer.count != 0:
    print('测试失败！')
else:
    bart = Volunteer('Bart', 'M')
    if Volunteer.count != 1:
        print('测试失败！')
    else:
        lisa = Volunteer('lisa', 'F')
        if Volunteer.count != 2:
            print('测试失败！')
        else:
            print('Vplunteer: ', Volunteer.count)
            print('测试通过！')