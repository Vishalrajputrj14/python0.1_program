
class ParentClass:
    def parent_method(self):
        print("This is a method in the parent class method")


class ChildClass(ParentClass):
    def parent_method(self):
        print("vishalrajput")
        return super().parent_method()
    def child_method(self):
        print("This is a method in the child class method")
        super().parent_method()


child = ChildClass()
child.child_method()
child.parent_method()


class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

class Programmer(Employee):
    def __init__(self, id, name, salary, language):
        super().__init__(id, name, salary)
        self.language = language

vishal = Employee("E001", "Vishal", 60000)
harry = Programmer("E002", "Harry", 70000, "Python")


print(vishal.id, vishal.name, vishal.salary)
print(harry.id, harry.name, harry.salary, harry.language)

