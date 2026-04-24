# class Employee:
#     def __init__(self):
#         self.name = input("Enter the name of the employee: ")
#         self.salary = float(input("Enter the salary of the employee: "))
#         self.department = input("Enter the department of the employee: ")
#         self.id = int(input("Enter the ID of the employee: "))
#         self.company = input("Enter the company of the employee: ")

#     def showDetails(self):
#         print(f"The name of the employee is: {self.name}")
#         print(f"Salary: {self.salary}")
#         print(f"Department: {self.department}")
#         print(f"ID: {self.id}")
#         print(f"Company: {self.company}")

        
# e = Employee()
# e.showDetails()



class Employee:
     def __init__(self):
          self.__name = "vishal"



a = Employee()
# print(a.__name) # Connot be accessed directly because it is private variable
print(a._Employee__name) # Can be accessed indirectly

print(a.__dir__()) # To see the name of the private variable in the class
        