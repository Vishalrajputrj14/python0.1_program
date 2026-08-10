# Recrison in python 

'''
Recrison is the process of defining something in terms 
of itself.

A physical world example would be to place two parallel
mirrors facing each other. Any object in between them
would be reflected recursively.

python Recursive function

In python We know that a funtion can call othern
funtion. It is even possible for the function to 
call itself These types of  construct are termed as recurisve
functions.


'''
# factorial(7) => 7*6*5*4*3*2*1
# factorial(6) => 6*5*4*3*2*1
# factorial(5) => 5*4*3*2*1
# factorial(4) => 4*3*2*1
# factorial(0) => 1

# f  factorial(n) * factorial(n-1)

def fectorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fectorial(n-1)

print(fectorial(3))
print(fectorial(4))
print(fectorial(5))


#example 2 
 
numTerms = int(input("Enter the number of terms: "))

n1, n2 = 0, 1

print("Fibonacci Sequence:")
for i in range(numTerms):
    print(n1, end=" ")
    nextTerm = n1 + n2
    n1 = n2
    n2 = nextTerm
