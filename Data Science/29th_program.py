def func1():  
    try: 
        l = [1,5,8,9,10]
        i = int(input("enter the index:  "))
        print(l[i])
        return 1

    except:
        print('Some error occurred')
        return 0

    finally: 
        print("I am always executed  ")


x = func1()
print(x)