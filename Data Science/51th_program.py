x = [1,2,3,4,5]
dir(x)
print(dir(x))
print(x.__add__)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("vishal", 25)
p1.__dict__
print(p1.__dict__)
print(help(Person))