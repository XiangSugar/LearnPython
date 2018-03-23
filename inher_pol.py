# -*- coding : utf-8 -*-
# 继承和多态

class Animal(object):
    def run(self):
        print('Animal is running......')
    
class Cat(Animal):
    def run(self):
        print('Cat is running......')

class Dog(Animal):
    def run(self):
        print('Dog is running......')

class Fish(Animal):
    pass

cat = Cat()
dog = Dog()
fish = Fish()

dog.run()
cat.run()
fish.run()