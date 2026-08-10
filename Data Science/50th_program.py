# Class Method as Alternative Constructor in Python




class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls, string):
        name, salary = string.split(" - ")
        return cls(name, int(salary))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromStr(cls, string):
        name, age = string.split(" - ")
        return cls(name, int(age))


e2 = Employee.fromStr("vishal - 60000")
print(e2.name, e2.salary)

p1 = Person.fromStr("vishal Doe - 25")
print(p1.name, p1.age)