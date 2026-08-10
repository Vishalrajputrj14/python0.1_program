class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def work(self):
        print(f"{self.name} is working as a {self.position}.")

class Programmer(Employee):
    def __init__(self, name, position, programming_language):
        super().__init__(name, position)
        self.programming_language = programming_language

    def code(self):
        print(f"{self.name} is coding in {self.programming_language}.")
    
e = Employee("Alice", "Developer")
e.work()  # Alice is working as a Developer.
e = Employee("vishal", "Developer")
e.work()  # Alice is working as a Developer.
e1 = Programmer("Bob", "Programmer", "Python")
e1.work()  # Bob is working as a Programmer.