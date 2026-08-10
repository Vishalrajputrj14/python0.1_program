# break statement 
'''
The break statement enables a program to ship over 
a part of the code. A break statement  terminates the 
very loop it lies within.
'''

for i in range(11):
    print(14 * i)
    if(i == 5):
        break
#exmple 2

for k in range(11):
    if(k == 5):
        break
    print(5 * k)

#exmple 3

for s in range(12):
    if(s == 7):
        break
    print("5 x ", s+1 , "=", 5*(s+1))
    print("loop ko chodkar nikal gaya")

#exmple 4

'''
Continue Statement 

The continue statement skips the rest of the loop 
statements and causes the next teration to occur.
'''

for v in range(12):
    if(v == 9):
        print("skip the iteration ")
        continue
    print("5 x", v+1 ,"=", 5 * (v*1))
        
    

