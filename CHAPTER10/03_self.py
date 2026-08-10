class Employee:
    language = 'Python'  # Corrected spelling
    salary = 1000000

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}, the name is {self.name}, and the age is {self.age}")

    def greet(self):
        print(f"Hello {self.name}, welcome to the company!")    

# Creating an instance of Employee
harry = Employee()
harry.name = 'Harry'
harry.age = 20

# Calling methods
harry.getinfo()
harry.greet()