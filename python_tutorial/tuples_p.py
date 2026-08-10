# python tuples
'''
tuples are ordered collection of data items. they store multiple items in a single 
varible. tuple items are separated by  commas and enclosed within round brackets 
(). tuples are unchangeable meaning we can mot alter them after creation.
'''


tup = (1,2,3, "vishal", 2500,250, 2352005)
print(tup)
print(type(tup))
print(len(tup))
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
if 21  in tup:
    print("yes 3 is present in this tuple ")
else:
    print("No 3 is upsent in thi tuple")

tup2 = tup[2: 7]
print(tup2)
'''
Tuples are immutable hence if you want to add, remove or change tuple 
items, them first you must convert the tuple to a list. 
then perform operation on that list and convert it back to tuple.
'''
# exapmle
countries =  ("Spain", "Italy", "India"," england", "germany")
temp = list(countries)
temp.append("india")  # add item 
temp.pop(3)  #Remove item 
temp[2] = "finland" # change item
countries = tuple(temp)
print(countries)

#example 

name = ("vishal", "yoegsh", "puneet" , "naman" , "rudra", "harsh", "utkarsh") 
girls = ("mahak", "nandni", "urvashi" , "chinee", "kajal" , "Mona" , "tanisha")

mynames = name + girls
print(mynames)

"tuples methods"
'''
As tuple is immutable type of collection of elemensts it have limited 
built in methods. they are explained below 

count() Method =>  

the count() memthod of tuple retuns the number of items the given 
element appeats in the tupls.
'''

#example 

tup_m = (0,1,2,3,4,5,6,7,8,9,5,5,5,22,2,2,2,2,4,4,4,4,) 
res = tup_m.count(5)
print("count of 3 in tuple1 is: =>  ", res)
res = tup_m.index(3,2,5)
print(res)