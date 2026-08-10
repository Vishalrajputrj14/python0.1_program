"""
factorial(1) = 1
factorial(2) = 1*2
factorial(3) = 3*2*1
factorial(4) = 4*3*2*1
factorial(5) = 5*4*3*2*1
factorial(n) = n * n-1 *......3*2*1

"""
def fectorial(n):
    if(n==1 or n==0):
        return 1
    return n * fectorial(n-1)


n = int(input("Entar a numbar:  "))
print(f"The factorial of this numbar is: {fectorial(n)}")