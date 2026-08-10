class employee:
    def __init__(self, name , age , salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    @classmethod
    def from_string(cls, emp_str):
        name, age, salary = emp_str.split("-")
        return cls(name, int(age), int(salary))


e = employee("Vishal", 24, 50000)
print(e.name)
print(e.age)
print(e.salary)

str_input = "Vishal-24-50000"
name, age, salary = str_input.split("-")
e2 = employee(name, int(age), int(salary))
print(e2.name)
print(e2.age)
print(e2.salary)