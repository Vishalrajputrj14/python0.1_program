def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Entar temperature in F :  "))
c = f_to_c(f)
# print(f_to_c(f))
# print(f"{f_to_c(f)}  °c") 
print(f"{round(c , 2)}  °c") 