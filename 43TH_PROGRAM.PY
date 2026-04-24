class Person: 
    name = "vishal rajput"
    occupation = "data scientist"
    networth = 1000000000
    def info(self):
        print(f"{self.name} is a {self.occupation} and has a net worth of {self.networth}")

a = Person()
# a.name = "vishu rajput"
# a.occupation = "data analyst"
# a.networth = 100000000

print(a.name, a.occupation, a.networth)
a.info()


class Employee:
    def __init__(self, n , o):
        print("employee created")   
        self.name = n
        self.occupation = o
        self.networth = 0

    def info(self):
        print(f"{self.name} is a {self.occupation} and has a net worth of {self.networth}") 

e1 = Employee("vishal rajput", "data scientist")
e1.info()
e1.networth = 1000000000
e1.info()
b = Employee("vishal rajput", "data analyst")
b.info()
c = Employee("vishal rajput", "data engineer")
c.info()
d = Employee("vishal rajput", "data architect")
d.info()