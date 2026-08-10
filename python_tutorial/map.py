def cube(x):
    return x * x  * x


print(cube(2))

l = [1 ,2 ,4 ,6 ,8 ,13] 
new = list(map(cube, l))
print(new)

#filter 



def filter_function(a):
    return a > 2


newnewl = list(filter(filter_function,l))
print(newnewl)



v = [ 2,5,4,9,12,36,98,89,87,78]


vishal = list(map(lambda x: x*x*x, l))
print(vishal)







