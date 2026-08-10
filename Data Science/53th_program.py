class Employee:
    name = "vishal"
    def __len__(self):
     i =  0
     for c in self.name:
         i  = i + 1
     return i
    


e = Employee()
print(len(e))
print(e.name)