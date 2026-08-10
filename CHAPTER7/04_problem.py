n = int(input("Entar a numbar :   "))

for  i  in range(2, n):
    if(n%i) == 0:
        print("Numbar is not prime")
        break
    else:
        print("Numbar is prime")

        