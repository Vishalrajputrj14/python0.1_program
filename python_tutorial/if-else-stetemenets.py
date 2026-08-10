 # if - else statements 
'''
sometimes the programmer needs to check the evaluation if certain  expression(s)) is true or false and then execute certain block of code based on the evaluation.
if the expression evaluates to false then the program execution folllows a different path than it than it would have if the expression had evalualted to true.

besed on this the conditional statements are further classified into following types: 

1. if statement
2. if-else statement
3. if-elif-else statement
4. nested if statement

'''
# Conditional operators  = >, <, >=, <=, ==, !=

A  = int(input("enter your age: "))
print("your age is: ", A)
if A>=18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")


print(A>18)
print(A<18)
print(A<=18)
print(A>=18)
print(A==18)
print(A!=18)


# An if.....else statement evaluates like this: 

'''if the expression evaluates true 
Execute this block of code inside if statement. After execution retrun to 
the code out of the if-else blook.
 if the expression evaluates false
Execute this block of code inside else statement. After execution return to
the code out of the if-else block.


'''
# example 2
ruslte = int(input("enter your marks: "))
if ruslte>=33:
        print("you are pass")
else:
        print("you are fail")


# example 3
applePrice = int(input("enter the price of apple: "))
budget = int(input("enter your budget: "))
if (applePrice<=budget):
        print("you can buy apple")
else:
        print("you can not buy apple")

# example 4

applePrice = int(input("enter the price of apple: "))
budget = int(input("enter your budget: "))
if (budget - applePrice > 50):
        print("you can buy apple")
elif (budget - applePrice > 70):
        print("you can buy apple but you have no money left")
else: 
        print("you can not buy apple")


# example 5
num = int(input("enter a number: "))
if (num%2==0):
        print("the number is even")
else:
        print("the number is odd")

# example 6
num = int(input("Enter the value of num:    "))
if (num <0):
       print("the number is negative")
elif (num ==0):
         print("the number is zero")
else:
         print("the number is positive")


# example 7 

num = 18
if(num <0):
         print("the number is negative")
elif(num >0):
        if(num <= 10):
                print("numbar is between 1-10")
                
                
        elif(num >10 and num <=20):
                print("number is between 11-20" )
        else:
                print("number is greater than 20")
else:
         print("the number is zero")


# example 8 
mode = input("enter the mode: ")
if(mode == "r"):
        print("the mode is read only")
elif(mode == "w"):
        print("the mode is write only")
elif(mode == "rw"):
        print("the mode is read and write")
elif(mode == "b"):
        print("the mode is blue")
else:
        print("invalid mode")

# example 9

