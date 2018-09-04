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
print(s.score)  # 实际转化为 s.get_score()

s.score = 999  # error

# --------------------------------------------------------------
class Screen(object):
    
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be integer!')
        if not 10 <= value <= 100:
            raise ValueError('width must between 10~100 !')
        self._width = value
        
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be integer!')
        if not 10 <= value <= 100:
            raise ValueError('height must between 10~100 !')
        self._height = value
        
    @property
    def resolution(self):
        return self._resolution
# -------------------------------------------------------------
