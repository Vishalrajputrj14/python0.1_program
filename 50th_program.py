# Class Method as Alternative Constructor in Python


class Employee:
    def __init__(self, name , salary):
        self.name = name
        self.salary = salary


    @classmethod
    def fromStr(cls , string):
        name, salary = string.split(" - ")[1]
        return cls(name, int(salary))
    
e1 = Employee("Alice", 50000)
print(e1.name)  # Output: Alice
print(e1.salary)  # Output: 50000


string = "vishal - 60000"
e2 = Employee.fromStr(string)
print(e2.name)  # Output: vishal
print(e2.salary)  # Output: 60000


class Parson :
    def __init__(self, name , age ):
         self.name = name
         self.age = age

    @classmethod
    def fromStr(cls , string):
        name, age = string.split(" - ")
        return cls(name, int(age))
    
p1 = Parson.fromStr("vishal Doe - 25")
print(p1.name, p1.age)  # Output: vishal 25