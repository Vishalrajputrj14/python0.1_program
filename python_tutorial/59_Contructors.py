'''
A constructor is a special method inn a class used to create and intialize an
object of a class. there are different types of constructors. constructors is invaked automatically when an object of a class is created.

A constructor is a unique funtion that gets called autimatically when an object is created of a class. the main 
purpose of a constructor is to initialize or assign valuse to the data members of that class. It cannot rerurn any 
value other than None.

'''

class parson:
    name = "vishal"
    occ  = "web developer"
    age  = 18
    def __init__(self, name, occ, age):  # parameterized constructor
        self.name = name
        self.occ = occ
        self.age = age
        

# print("this is parameterized constructor")
# delets = parson("yogesh", "shop wala", 20)
# print(delets.name)
# print(delets.occ)
# bb = parson()


# print(bb.name)
# print(bb.occ)
# print(bb.age)



class parson1:
    name = "vishal"
    occ  = "web developer"
    def info(self):
        print(f"{self.name} is a {self.occ}") 

a = parson1()

print(a.name)
a.info()
a.name = "yogesh"
a.occ = "shop wala"
a.info()
print(a.name)
print(a.occ)


class parson:
    def __init__(self):
        print("this is non parameterized constructor")
        self.name = "vishal"
        self.occ  = "web developer"
        self.age  = 18
    def info(self):
        print(f"{self.name} is a {self.occ}")


bb = parson()
print(bb.name)
print(bb.occ)


# python tutorial 59 classes and objects  => Decorators




def greet(fun): 
    def fun1():
        print("good morning")
        fun()
        print("thanks for using this function")
    return fun1   # yaha hona chaiye

@greet
def hello():
    print("hello world")

def add(a, b):
    print(a + b)

hello()
