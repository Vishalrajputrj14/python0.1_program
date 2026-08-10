# Exception Handling 
'''
Exception  handling is the process of responding to unwanted or unexpected 
events when a computer program runs. Exception handling  deals with these 
events to avoid the program or system crashing , and without this process,
exceptions would disrupt the normal operatio of  a program.




Exception in python


python has many bulit-in exceptions that are raised when your program 
encounters an error (something in  the program goes wrong).

When these exceptions occur, the python interperter stops the current process
and passes it to the calling process until it is handled. If not handled ,the 
program will crash.


python try.. execpt 


try except blocks are used in python to handle errors and exceptions. the 
code in try block runs when there is no error. If the try block catches the 
error, then the except block is executed. 


'''

# a  =  input("Entar the numbar ")
# print(f"Maltiplicstion table of {a} is :")
# try: 
#     for i in range(1,11):
#      print(f"{int(a)} * {i} = {int(a)*i}")
# except Exception as e:
#     print(e)




# print("Some imp linse of code ")
# print("End of program") 

# example 2


# try:
#     a = int(input("Enter the number: "))
#     print(f"Multiplication table of {a} is:")
#     for i in range(1, 11):
#         print(f"{a} * {i} = {a * i}")
# except ValueError:
#     print("Please enter a valid integer!")

# print("Some imp lines of code")
# print("End of program")


# example 2
 

try:
    num = int(input("Entar an integer:  "))
    a = [6,6]
    print(a[num])
except ValueError :
        print("Numbar entered is not an integer ")

except IndexError:
    print("Index Error ")