class  Employee: 
    company = "Google"
    def show(Self):
        print(f"The name is {Self.name} and the company is {Self.company}")
    @classmethod
    def changeCompany(Cls, newCompany):
        Cls.company = newCompany


emp1 = Employee()
emp1.name = "Alice"
emp1.show()  # Output: The name is Alice and the company is Google
emp1.changeCompany("Tesla")
emp1.show()  # Output: The name is Alice and the company is Tesla
emp2 = Employee()
emp2.name = "VISHALRAJPUT"
emp2.show()  # Output: The name is VISHALRAJPUT and the company is Google
