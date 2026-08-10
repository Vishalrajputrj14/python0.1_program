 # python lists 
'''
. List are ordered collection of data items.
. they store multiple items in a single variable.
. list items are separated by commas and enclosed
within square brackets[].
. lists aar changeable meaning we can alter them after creation.
 

'''
marks = [3,2,4,7,"vishal", True ]
print(marks)
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])
# List Index 
''' 
Each item/element in a list has its own unque index. this index can be 
used to access any particular item from the list. The first item has index[0], second item has index[1], third item has index[2]and so on. 

'''
# example:

colors = ["rad", "Green", "Blue", "yellow", "green"]
#          [0]      [1]      [2]     [3]       [4]

# Accessing list items

'''
We can access list items by using its index with the square bracket syntax[]. 
for example colors[0] will give "rad" , colors[1] will give "green"
and so on....
'''
# example 3 

print(marks[-3]) # Negative index 
print(marks[len(marks)-3]) # positive index 
print(marks[5-3]) # positive index 
print(marks[2]) # positive index 


# example 4 
if "vishal"  in marks:
    print("yes")
else:
    print("no") 

l = [ 1,2,3,4,5,6,5,8,5,5]
print(type(l))
print(l)
l.append(7)
print(l)
l.sort(reverse=True)
print(l)
print(l.index(3))
print(l.count(5)) 
m = l.copy()
m[0] = 0
l.insert(1,998)
m = [900,1000,1100]
k = l + m
print(k)
print(l)