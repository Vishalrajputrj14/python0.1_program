"""


* * *      for n = 3
*   *
* * *



"""
n = int(input("enter the numbar :  "))
for i in range(1, n+1):
    if(i==1 or i==n):
        print(" *"*n, end="")
    else:
        print("*", end="")
        print(" "* (n-2),end="")
        print("*", end="")
        print(" ")


def print_pattern(n):
    for i in range(1, n+1):
        if i == 1 or i == n:
            print("* " * n)
        else:
            print("*" + " " * (2*n - 3) + "*")

n = int(input("Enter the number: "))
print_pattern(n)