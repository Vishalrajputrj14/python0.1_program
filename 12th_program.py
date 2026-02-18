# a = int(input("Enter your age : "))
# print("Your age is : ", a)
# # Conditional operators in python
# # print(a>18) 
# # print(a<18)
# # print(a==18)
# # print(a<=18)
# # print(a>=18)
# # print(a!=18)


# if(a > 18):
#     print("You con drive a car")
#     print("yes")
# else:
#     print("You can not drive a car")
#     print("no")
#     print(" chalane de na bodke ke ")

# appleprice = 210
# budget = 200
# if appleprice <= budget:
#     print("You can buy the apple")
# else:
#     print("You can not buy the apple")


num = int(input("Enter a number : "))
if (num < 0):
    print("The number is negative")
elif(num == 999):
    print("The number is special")
else:
    print("The number is positive")

# Nested if else statement 

num = 25
if(num < 0):
    print("The number is negative")
elif(num > 0):
    if(num <= 10):
        print("Number is between 1-10")
    elif(num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("The number is zero")