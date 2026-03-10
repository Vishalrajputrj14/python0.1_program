a = input("Entar the number :  ")
print(f"multiplication table if {a} is :   ")

try: 
    for i in range(1,11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except Exception  as e:
    print(e)



print("Some imp lines of code")
print("End of program")





