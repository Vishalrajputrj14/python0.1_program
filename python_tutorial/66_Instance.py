'''
Instance vs Class Variables in Python

In python, variables can be defined at the class or at the instance level.
Understanding the difference between these of variables is crucial for writing 
efficiengt and maninteinable code.

Class Variables:
class variables are defined at the class level and are shared among all 
instances of the class. They are defined outside of any method and are usually used to 
store information that is common to all instances if the class. for example: 
a class variable can be used to store the number of instances of a class that have been crated.




'''

class Employee:
    compnay = "Google"  # Class Variable
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position  # Instance Variables

    def showdetails(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Position: {self.position} , companyname {self.compnay}")

e1 = Employee("Vishal", 50000, "Developer")
e1.showdetails()
 