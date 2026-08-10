class Student:
    def __init__(self):
        self.name = "John"        # public attribute
        self._age = 20            # protected attribute
        self.__grade = 'A'        # private attribute
    def _funName(self):      # protected method
        return "This is a protected method"
    
class subject(Student): #class inheriting from Student class
      pass 

s = Student()
s1 = subject()
print(s.name)          # Accessing public attribute
print(s._age)         # Accessing protected attribute (conventionally should be accessed within

                        # class or subclass                     
print(s._Student__grade) # Accessing private attribute (name mangling)
print(s._funName())    # Accessing protected method (conventionally should be accessed
                        # within class or subclass      
print(s1._age)         # Accessing protected attribute from subclass
print(s1._funName())    # Accessing protected method from subclass
                        # within class or subclass                              