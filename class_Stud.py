# -*- coding: utf-8 -*-
# OOP 面向对象编程

# 类的定义
# (object)表示该类是从哪个类继承下来的，如果没有合适的继承类，就使用object类
# 这是所有类都会继承的类
class Student(object):

    # 绑定属性，第一个参数永远是self,表示创建的实例本身
    # 在__init__方法内部，就可以把各种属性绑定到self
    # 有了__init__方法，在实例创建的时候，就不能传入空的参数，
    # 必须传入与之匹配的参数, self 不用传
    def __init__(self, name, score, gender):
        self.__name = name
        self.__score = score
        self.__gender = gender
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score > 60:
            return 'B'
        else:
            return 'C'
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def get_gender(self):
        return self.__gender
    def set_name(self, name):
        self.__name = name
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('Bad score!')
    def set_gender(self, gender):
        self.__gender = gender


# 实例化Student类
bart = Student('Bart', 59, 'M')
lisa = Student('Lisa', 89, 'F')

bart.print_score()
lisa.print_score()
print(lisa.get_name(), lisa.get_grade())

bart.set_score(99)
print(bart.get_name(), bart.get_score())

# 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，
# 并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，
# 所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。