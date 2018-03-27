# -*- coding: utf-8 -*-
# The use of property

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be integer!')
        if not 0 <= value <= 100:
            raise ValueError('score nust between 0~100!')
        self._score = value

s = Student()
s.score = 66  # 实际转化为s.set_score(60)
print(s.score)

s.score = 999
