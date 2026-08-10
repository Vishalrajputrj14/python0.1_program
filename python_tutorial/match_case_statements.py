'''
Match Case Statements
To implement switch-case like characteristics very similar to if-else functionality, we use a match case in python.
 If you are coming from a C, C++ or Java like language, you must have heard of 
switch-case statements. If this is your first language, dont worry as 
I will tell you everything you need to know about match case statements in this video!

A match statement will compare a given variable’s value to different 
shapes, also referred to as the pattern. The main idea is to keep on
 comparing the variable with all the present patterns until it fits into one.

The match case consists of three main entities :

The match keyword
One or more case clauses
Expression for each case
The case clause consists of a pattern to be matched to the variable, 
a condition to be evaluated if the pattern matches, and a set of
 statements to be executed if the pattern matches.

Syntax:
'''

x = int(input("Enter a number between 1 and 5: "))
match x:
    case 1:
        print("You entered One")
    case 2:
        print("You entered Two")
    case 3:
        print("You entered Three")
    case 4:
        print("You entered Four")
    case 5:
        print("You entered Five")
    case _:
        print("Number not in range")
#example 2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

result = None
match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    case _:
        result = "Invalid operation"
print("Result:", result)

#example 3

a =  int(input("Enter your state code:    "))
passward = None
if ( a == 321001):
    passsward =  "the right passward in your state"
elif ( a == 3001 ):
    passsward =  "the right passward in your state in jaipur"
elif (a == 450001):
    passsward = "the right passward in your state in indore"
elif (a == 110001):
    passsward = "the right passward in your state in delhi"
elif (a == 500001):
    passsward = "the right passward in your state in hyderabad"
else:
    passsward = "you are not in india"  
print(passsward)


    
     


       