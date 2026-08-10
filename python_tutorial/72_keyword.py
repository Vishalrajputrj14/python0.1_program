class ParentClass:
    def parent_method(self):
        print ( "This is the parent method.")

class ChildClass(ParentClass):
    def parent_method(self):
        print("vishal is a good boy")
        super().parent_method()
    def child_method(self):
        print("This is the child method.")
        super().parent_method()




child_obj = ChildClass()
child_obj.parent_method()
child_obj.child_method()


class Employee:
    def __init__(self, name , age , salary):
        self.name = name
        self.age = age
        self.salary = salary
    
 
class Programmer(Employee):
    def __init__(self, name, age, salary, language):
        super().__init__(name, age, salary)
        self.language = language

 
rohan = Employee("Rohan", 24, 50000)
print(rohan.name)
print(rohan.age)
print(rohan.salary)
programmer1 = Programmer("Vishal", 24, 60000, "Python")
print(programmer1.name)
print(programmer1.age)
print(programmer1.salary)   
print(programmer1.language)
# str_input = "Vishal-24-50000"
# name, age, salary = str_input.split("-")
# e2 = Employee(name, int(age), int(salary))