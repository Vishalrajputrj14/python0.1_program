'''
python while loop 


As the name suggests, while loops execute a statements while the condition is true. As soon as the condition becomes false, the 
interpeter comes out of the while loop.


'''

# example 1

i = 1 
while (i < 5):
    print(i)
    i = i + 1
# example 2
i = int(input("enter a number"))
while (i <= 50):
    i = int(input("enter a number"))
    print(i)
    i = i + 1
# example 3
count = 5
while (count > 0):
    print("countdown:", count)
    count  = count - 1

''' 
Hera , the count variable is set to 5 which decrements after each iteration.
Depending upon the while loop codition, we need to either increment or decrment the 
the counter variable( the variable count , in our case ) or the loop will continue 
forever.
'''

# example 4
v = 5 
while (v > 0):
    print("value of v is:", v)
    v = v - 1

'''
else with while loop 


We can even use ese statement with the whie loop. Essentially what the else statement 
does is that as soon as the while  loop condition 
becomes False the interpreter comes out of the while loop
and else statement is executed.

'''
#else with while loop 
# example 5

numbar = 10
while (numbar >0):
    print("numbar is:", numbar)
    numbar = numbar - 1
else:
    print("the numbar is no longer greater than zero")

# example 6
 
 # Table using while loop

num = int(input("Enter a number: "))
i = 1

while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1

