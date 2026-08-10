'''
In python is and == are both coparison operators that can be used to check if two valuse are equal. However there are some important differences between the two that you should be aware of. 

the is operator compares the identity of two objects, while
the ==operator compares the valuse of the objects this means that is will only return true if the objects being 
compared are the exact same object in memory, while == will return True of the objects have the same value 
'''


a = (2,10,151)
b = (2,10,150)
print(a is b) # exact location of object in memory
print(a == b) # value