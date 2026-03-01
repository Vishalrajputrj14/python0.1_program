def geometric_mean(x, y):
    gmean = (x*y)/(x+y)
    return gmean

print("The geometric mean of 9 and 8 is: ", geometric_mean(2, 8))

def isGreater(a, b):
    if a > b:
        print("first number is greater than")
    else:
        print("second number is greater than")


isGreater(9, 8)
isGreater(7, 6)
isGreater(5, 10)

v = 9 
M = 8
if(v > M):
    print("first number is greater than")
else:
    print("second number is greater than")
a = 9
b = 8
gmean1 = (a*b)/(a+b)
print("The geometric mean of a and b is: ", gmean1)
c = 7
d = 6
gmean2 = (c*d)/(c+d)
print("The geometric mean of c and d is: ", gmean2)
