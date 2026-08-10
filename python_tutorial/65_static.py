'''
Static methods in python are methods that belong to a class rather 
than an instance of thr class. They are defined using the @statcmethod decorator and 
do not have access to the instance of the class (i.e. self) they are called on the class 
itself, not on an instance of the class static methods are often used to create utility funtions that don't need access to instance data


'''

class Math:
    def __init__(self, value):
        self.value = value

    def addtounum(self, num):
     self.value = self.value + num


    @staticmethod
    def add(x, y):
        return x + y
    

a = Math(5)
a.addtounum(10)
print(a.value)
print(Math.add(5, 10))
print(a.add(5, 10))  # This will also work but is not the preferred way to call static methods
    
