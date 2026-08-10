
def fuc1():

    try: 

        l = [1,5,6,7,8]
        i = int(input("Entar the index:  "))
        print(l[i])
    except:
         print("Some error occurred")
         return 0

    finally:    
        print("i am always executed ")
        print(" i am always executed")


x = fuc1()
print(x)