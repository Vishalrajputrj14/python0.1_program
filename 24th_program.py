# 

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(3)
print(factorial(5))
print(factorial(30))
print(factorial(56))
print(factorial(91))
print(factorial(25))

numterms =int(input("enter the number of terms   "))
n1 = 0
n2 = 1
nexttrems = None
print("Fibonacci serise")
for i in range(numterms):
    print(n1)
    nexttrems = n1 + n2
    n1 = n2
    n2 = nexttrems

print(n1)
print(n2)






