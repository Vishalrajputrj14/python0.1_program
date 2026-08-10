class Employee:
    def __init__(self, name, salary, department, id, company):
        self.name = name
        self.salary = salary
        self.department = department
        self.id = id
        self.company = company
        
    def showDetails(self):
        print(f"The name of the employee is: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")
        print(f"ID: {self.id}")
        print(f"Company: {self.company}")


e = Employee("John Doe", 50000, "IT", 12345, "Tech Company")
e.showDetails()


