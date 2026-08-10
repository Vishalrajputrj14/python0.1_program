def cube(x):
    return x*x*x




print(cube(2))




l = [1,2,3,4,5,8]
newl = []
for item in l:
    newl.append(cube(item))

    print(newl)
newl= list(map(cube , l))
print(newl)


# FILTER

def filter_fuction(a):
    return a>4

newnewl = list(filter(filter_fuction, l))
print(newnewl)

from functools import reduce
#  list of numbers 
numbers = [1,2,3,4]
numbers = [1,2,3,4]

# Calculate the sum if the numbers using the reduce fuction 
def mysum(x,y):
    return x+y


sum = reduce(mysum, numbers)

print(sum)