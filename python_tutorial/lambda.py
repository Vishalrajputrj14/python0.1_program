# lambda funtions in python 

'''
In python, a lambda funtion is a small anonymouse function without a name. It is defined using the lambda keyword and has the following 

syntax:   lambda arguments: expression


lambda funtion are often used in situations where a small funtion is required for a short period of time. they are commmonly used as arguments to higher-order funtions such as map , filter, and reduce.

'''

def double(x):
    return x*2



print(double(5))


double = lambda x: x*2
cube = lambda s: s*s*s
avg = lambda z, y: (z+y)/2
avgg = lambda z, y, v: (z + y + v)/3

print(double(10))
print(cube(7))
print(avg(3,5))
print(avgg(3,5,10))