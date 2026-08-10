'''
function Arguments and return statament


There are four types of arguments that we can provide in a funtion: 

1. Default Arguments 
2. Keyword Argumemts 
3. Varibale length Arguments
4. Required Arguments

Default argumemts: 

We can provide a defaukt value whilw creatng a function . this way the funtion
assumes a default value even if a value is not provided in the funtion call for that
argument.


'''


#exmple 
def avarage(a, b):
    print("The average is ", (a+b)*2)

avarage(4,6)

#exmple 2  keyword arguments:

'''
We can provide arguments with key = value, this way the 
interpreter recoginzes the arguments by the paraneter name.
hence, the the order in which the arguments are passed does 
not matter.
'''

def name(fname, mname = "jhon", lname = "whatson"):
    print("hello", fname , mname, lname)


name("vishal", "rajput")

#exmple Required arguments: 
'''
In case we din't pass the arguments with a key = valus syntax,
then it is necaessary to pass the arguments in the correct 
positional order and the numbar of argumnets passed shouldn
match with actual function defintion. 
'''

def average(*numbars):
    sum = 0
    for i in numbars:
        sum = sum + i 
    print("Averagev is: ", sum/len(type(numbars)))

avarage(5, 6)

#exmple 


def name(**name):
    print(type(name))
    print("hello", name["fname"],
          name["mname"], name["lname"])
name(mname = "vishal", lname = "yoegsh", fname = "bhalu ")