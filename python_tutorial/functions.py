'''
python funtions 

A funtions is a block of code that performs a specific task 
whenever it called . In bigger programs, where we have large 
amounts of code , it is advisable to create or use existing 
funtions that make the program flow orfanized and neat .

there are two types of function :

1. built - in funtions 
2.User-defined functions 


built - in funtions :
 these funtions are defined and pre-coded in python. Some 
 exmples of uilt-in funtions are follows:
 min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(),
 set(), print(), etc.
'''

'''
user - difined funtions :

We can create functions  to perfrom specific tasks as per out 
needs. suvh functions are called user-defined functions.

'''


def caluculaterGean(a, b):
    vishal = (a * b) / (a + b)
    print("Result:", vishal)

# values
a = 10
b = 4

# function call
caluculaterGean(a, b)
# exmple 2 

c = 12
d = 10
def isgreater(c, d):
    if(a>b):
        print("first numbar is greater")
    else:
        print("Second numbar is greater or equal")

isgreater(a, b)


